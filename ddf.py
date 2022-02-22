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
    ],
    "OBJECTIVE": [
        {
            "key": "O_1",
            "objective_desc": "To assess the safety of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients"
        },
        {
            "key": "O_2",
            "objective_desc": "To assess the effect of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients who have failed to 1st-line chemotherapy and are in second phase of disease"
        },
        {
            "key": "O_3",
            "objective_desc": "To assess the effect of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients who have failed to 1st-line chemotherapy"
        }
    ],
    "STUDY_CELL": [
        {
            "key": "SC_1"
        },
        {
            "key": "SC_2"
        },
        {
            "key": "SC_3"
        },
        {
            "key": "SC_4"
        }
    ],
    "STUDY_ARM": [
        {
            "key": "SA_1",
            "study_arm_description": "AZD6738 + Olaparib",
            "study_arm_name": "OLAPARIB_ADDON"
        },
        {
            "key": "SA_2",
            "study_arm_description": "AZD6738 + Durvalumab",  
            "study_arm_name": "DURVALUMAB ADD_ON"
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
    ],
    "HAS_OBJECTIVE": [
        {"from": "SD_1", "to": "O_1"},
        {"from": "SD_1", "to": "O_2"},
        {"from": "SD_1", "to": "O_3"},
    ],
    "HAS_CELL": [
        {"from": "SD_1", "to": "SC_1"},
        {"from": "SD_1", "to": "SC_2"},
        {"from": "SD_1", "to": "SC_3"},
        {"from": "SD_1", "to": "SC_4"},
    ],
    "HAS_ARM": [
        {"from": "SC_1", "to": "SA_1"},
        {"from": "SC_2", "to": "SA_2"}
    ],
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


