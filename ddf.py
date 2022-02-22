from neo4j import GraphDatabase

the_nodes = {
    "STUDY": [
        {
            "key": "S_1",
            "study_title": "Umbrella Study of DDR (DNA-Damage Response) Targeting Agents in Advanced Biliary Tract Cancer",
            "study_version": "???",
            "study_tag": "???",
            "study_status": "???"
        }
    ],
    "STUDY_IDENTIFIER": [
        {
            "key": "SI_1",
            "name": "ClinicalTrials.gov",
            "id_type": "RegistryID",
            "org_code": "NCT04298021"
        },
        {
            "key": "SI_2",
            "name": "ClinicalTrials.gov",
            "id_type": "RegistryID",
            "org_code": "NCT04298023"
        },
        {
            "key": "SI_3",
            "name": "SponsorNo",
            "id_type": "SponsorID",
            "org_code": "AZ002020202"
        }
    ],
    "STUDY_TYPE": [
        {
            "key": "ST_1",
            "study_type_classification": "INTERVENTIONAL"
        }
    ],
    "STUDY_PHASE": [
        {
            "key": "SP_1",
            "study_phase_desc": "PHASE II TRIAL"
        }
    ],
    "STUDY_PROTOCOL": [
        {
            "key": "SPR_1",
            "brief_title": "DDR", 
            "official_title": "Targeting Agents in ABTC",
            "PublicTitle": "DDR-Umbrella Study of DDR (DNA-Damage Response) Targeting Agents in Advanced Biliary Tract Cancer Umbrella ABTC Study",
            "scientific_title": "DDR-Umbrella Study of DNA-Damage Response Targeting Agents in Advanced Biliary Tract Cancer",
            "amendments": ""
        }
    ],
    "STUDY_DESIGN": [
        {
            "key": "SD_1"
        }
    ],
    "INVESTIGATIONAL_INTERVENTIONS": [
        {
            "key": "II_1",
            "intervention_desc": "Olaparibstring"
        },
        {
            "key": "II_2",
            "intervention_desc": "Durvalumab"
        },
        {
            "key": "II_3",
            "intervention_desc": "AZD6738"
        }
    ],
    "CODE": [
        {
            "key": "C_1",
            "code": "249565666",
            "code_system": "PubChem",
            "code_system_version": "09/02/2021",
            "decode": "Durvalumab; Imfinzi; Anti-B7H1; Monoclonal Antibody"
        },
        {
            "key": "C_2",
            "code": "L01XC28",
            "code_system": "ATC",
            "code_system_version": "14-12-2021",
            "decode": "Durvalumab"
        },
        {
            "key": "C_3",
            "code": "L01XK01",
            "code_system": "ATC",
            "code_system_version": "14-12-2021",
            "decode": "Olaparib"
        }
    ]
}

the_relationships = {
    "HAS_IDENTIFIER": [
        {"from": "S_1", "to": "SI_1"},
        {"from": "S_1", "to": "SI_2"},
        {"from": "S_1", "to": "SI_3"},
    ],
    "HAS_STUDY_TYPE": [
        {"from": "S_1", "to": "ST_1"},
    ],
    "HAS_STUDY_PHASE": [
        {"from": "S_1", "to": "SP_1"},
    ],
    "HAS_PROTOCOL": [
        {"from": "S_1", "to": "SPR_1"},
    ],
    "HAS_STUDY_DESIGN": [
        {"from": "S_1", "to": "SD_1"},
    ],
    "HAS_INVESTIGATIONAL_INTERVENTION": [
        {"from": "SD_1", "to": "II_1"},
        {"from": "SD_1", "to": "II_2"},
        {"from": "SD_1", "to": "II_3"},
    ],
    "HAS_CODED": [
        {"from": "II_1", "to": "C_3"},
        {"from": "II_2", "to": "C_1"},
        {"from": "II_2", "to": "C_2"},
    ]
}

def clear(tx):
    tx.run("MATCH (n) DETACH DELETE n")

#def print_friends(tx, name):
#    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
#                         "RETURN friend.name ORDER BY friend.name", name=name):
#        print(record["friend.name"])

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))

with driver.session() as session:
    session.write_transaction(clear)
    for key, value in the_nodes.items():
        query = "UNWIND $nodes as data CREATE (n:%s) SET n = data;" % (key)
        print(query)
        result = session.run(query, nodes=value)

    for key, value in the_relationships.items():
        query = "UNWIND $rels as data MATCH (n {key: data.from}) MATCH (m {key: data.to}) CREATE (n)-[:%s]->(m)" % (key)
        print(query)
        result = session.run(query, rels=value)

driver.close()


