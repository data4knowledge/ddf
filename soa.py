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
    print(query)
    result = session.run(query)
    print(result)
    visits = {}
    epoch_visits = {}
    epoch_count = 0
    for record in result:
        print("'%s', '%s'" % (record["epoch"], record["visit"]))
        if not record["epoch"] in epoch_visits:
            epoch_visits[record["epoch"]] = []    
            epoch_count += 1
        epoch_visits[record["epoch"]].append(record["visit"])
        visits[record["visit"]] = record["epoch"]
    print(epoch_visits)
    print(visits)

    # Activities
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
        -[]->(v:VISIT)<-[]-(wfi:WORKFLOW_ITEM) WHERE pr.brief_title = '%s'
        WITH wfi.description as activity ORDER BY v.number
        RETURN DISTINCT activity""" % (protocol_name)
    print(query)
    result = session.run(query)
    print(result)
    activities = []
    for record in result:
        print("'%s'" % (record["activity"]))
        activities.append(record["activity"])
    print(activities)

driver.close()

# Display the SoA
table = BeautifulTable()
table.columns.header = [""] + list(visits.values())
table.rows.append([""] + list(visits.keys()))
for activity in activities:
    table.rows.append([activity] + [''] * visits.__len__())
table.maxwidth = 180
print(table)
