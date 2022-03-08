# Code for generating an SoA from a DDF graph database
# Code has been quickly put together to get the desired outputs rather than
# making the code as elegant. It might be possible to merge the queries or 
# have them return more easily consumed results

from neo4j import GraphDatabase
from beautifultable import BeautifulTable

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))

with driver.session() as session:

    # Choose a protocol from DB
    protocol_name = "DDR"

    # Data
    visits = {}
    visit_row = {}
    visit_rule = {}
    epoch_visits = {}
    epoch_count = 0

    # Epochs and Visits
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->
        (e:STUDY_EPOCH)-[]->(v:VISIT) WHERE pr.brief_title = '%s'
        WITH e.study_epoch_name as epoch,v.name as visit ORDER BY e.sequence_in_study, v.number
        RETURN DISTINCT epoch, visit""" % (protocol_name)
    result = session.run(query)
    for record in result:
        if not record["epoch"] in epoch_visits:
            epoch_visits[record["epoch"]] = []    
            epoch_count += 1
        epoch_visits[record["epoch"]].append(record["visit"])
        visits[record["visit"]] = record["epoch"]
        visit_row[record["visit"]] = ""

    # Visit Rules
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
        -[]->(v:VISIT) WHERE pr.brief_title = '%s'
        WITH v ORDER BY v.number
        MATCH (v)-[:HAS_START_RULE]->(sr:RULE)
        MATCH (v)-[:HAS_END_RULE]->(er:RULE)
        RETURN v.name as visit,sr.rule_desc as start_rule,er.rule_desc as end_rule""" % (protocol_name)
    result = session.run(query)
    for visit in visits.keys():
        visit_rule[visit] = ""
    for record in result:
        if record["start_rule"] == record["end_rule"]:
            visit_rule[record["visit"]] = "%s" % (record["start_rule"])
        else:
            visit_rule[record["visit"]] = "%s to %s" % (record["start_rule"], record["end_rule"])

    # Activities
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
        -[]->(v:VISIT)<-[]-(wfi:WORKFLOW_ITEM)-[]->(a:ACTIVITY) WHERE pr.brief_title = '%s'
        WITH a.description as activity, v.name as visit ORDER BY v.number
        RETURN DISTINCT activity, visit""" % (protocol_name)
    result = session.run(query)
    activities = {}
    for record in result:
        if not record["activity"] in activities:
            activities[record["activity"]] = visit_row.copy()
        activities[record["activity"]][record["visit"]] = "X" 

    # Activity Order
    activity_order = []
    query = """MATCH path=(a:ACTIVITY)-[r:HAS_PREVIOUS_ACTIVITY]->(b:ACTIVITY) RETURN b.description as desc ORDER BY LENGTH(path) ASC;"""
    result = session.run(query)
    for record in result:
        activity_order.append(record["desc"])
    #print(activity_order)
    #print(activities.keys())

driver.close()

# Display the SoA
table = BeautifulTable()
table.columns.header = [""] + list(visits.values())
table.rows.append([""] + list(visits.keys()))
table.rows.append([""] + list(visit_rule.values()))
for activity in activity_order:
    if activity in activities:
        data = activities[activity]
        table.rows.append([activity] + list(data.values()))
table.maxwidth = 210
print("")
print("")
print("Schedule of Assessmments for %s" % (protocol_name))
print("")
print(table)
print("")
print("")