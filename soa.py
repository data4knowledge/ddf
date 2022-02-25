from neo4j import GraphDatabase
from beautifultable import BeautifulTable

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))

with driver.session() as session:

    # Choose a protocol from DB
    protocol_name = "DDR"

    # Epochs and Visits
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->
        (e:STUDY_EPOCH)-[]->(v:VISIT) WHERE pr.brief_title = '%s'
        WITH e.study_epoch_name as epoch,v.name as visit ORDER BY e.sequence_in_study, v.number
        RETURN DISTINCT epoch, visit""" % (protocol_name)
    #print(query)
    result = session.run(query)
    #print(result)
    visits = {}
    visit_row = {}
    epoch_visits = {}
    epoch_count = 0
    for record in result:
        #print("'%s', '%s'" % (record["epoch"], record["visit"]))
        if not record["epoch"] in epoch_visits:
            epoch_visits[record["epoch"]] = []    
            epoch_count += 1
        epoch_visits[record["epoch"]].append(record["visit"])
        visits[record["visit"]] = record["epoch"]
        visit_row[record["visit"]] = ""
    #print(epoch_visits)
    #print(visits)

    # Activities
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
        -[]->(v:VISIT)<-[]-(wfi:WORKFLOW_ITEM) WHERE pr.brief_title = '%s'
        WITH wfi.description as activity, v.name as visit ORDER BY v.number
        RETURN DISTINCT activity, visit""" % (protocol_name)
    #print(query)
    result = session.run(query)
    #print(result)
    activities = {}
    for record in result:
        #print("'%s', '%s'" % (record["activity"], record["visit"]))
        if not record["activity"] in activities:
            activities[record["activity"]] = visit_row.copy()
        activities[record["activity"]][record["visit"]] = "X" 
    #print(activities)

    # CRF Link
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
        -[]->(v:VISIT)<-[]-(wfi:WORKFLOW_ITEM)-[]->(a:ACTIVITY)-[]->(data:STUDY_DATA) WHERE pr.brief_title = '%s'
        WITH wfi.description as activity, data.ecrf_link as link
        RETURN DISTINCT activity, link""" % (protocol_name)
    #print(query)
    result = session.run(query)
    #print(result)
    crf_activities = {}
    for record in result:
        print("'%s', '%s'" % (record["activity"], record["link"]))
        if not record["activity"] in crf_activities:
            crf_activities[record["activity"]] = []
        crf_activities[record["activity"]].append(record["link"])
    print(crf_activities)

driver.close()

# Display the SoA
table = BeautifulTable()
table.columns.header = [""] + list(visits.values())
table.rows.append([""] + list(visits.keys()))
for activity, data in activities.items():
    table.rows.append([activity] + list(data.values()))
table.maxwidth = 210
print("")
print("")
print("Schedule of Assessmments for %s" % (protocol_name))
print("")
print(table)
print("")
print("")

# Display the CRF
import urllib.request

for activity, links in crf_activities.items():
    for link in links:
        if link != "":
            with urllib.request.urlopen(link) as f:
                xml = f.read().decode('utf-8')
                print(link)
                print(xml)