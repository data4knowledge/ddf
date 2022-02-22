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
    "STUDY_ARM": [
        {   "key": "ARM02",
            "study_arm_description": "AZD6738 + Durvalumab",
            "study_arm_name": "DURVALUMAB ADD_ON",
            "study_arm_tyåe": "TREATMENT ARM"
        },
        {
            "key": "ARM03",
            "study_arm_description": "AZD6738 + Olaparib",
            "study_arm_name": "OLAPARIB_ADDON",
            "study_arm_type": "TREATMENT ARM"	
        },
        {
            "key": "ARM04",
            "study_arm_description": "AZD6738 + emerging Therapy 1",
            "study_arm_name": "NEW1_ADDON",
            "study_arm_type": "TREATMENT ARM"		
        },
        {
            "key": "ARM05",
            "study_arm_description": "AZD6738 + emerging Therapy 2",
            "study_arm_name": "NEW2_ADDON",
            "study_arm_type": "TREATMENT ARM"
        }
    ],
    "STUDY_EPOCH": [
        {
            "key": "EPO004",
            "study_epoch_desc":	"Screening",
            "study_epoch_name":	"SCREEN",
            "study_epoch_type":	"Screening"
        },
        {
            "key": "EPO005",
            "study_epoch_desc":	"Run-In",
            "study_epoch_name":	"RUN-IN",
            "study_epoch_type":	"Run-IN"
        },
        {
            "key": "EPO006",
            "study_epoch_desc":	"Treatment Cycle 1",
            "study_epoch_name":	"TREATMENT",
            "study_epoch_type":	"Treatment 1"
        },
        {
            "key": "EPO007",
            "study_epoch_desc":	"Treatment Cycle 2",
            "study_epoch_name":	"TREATMENT",
            "study_epoch_type":	"Treatment 2"
        },
        {
            "key": "EPO008",
            "study_epoch_desc":	"Following Cycles",
            "study_epoch_name":	"TREATMENT",
            "study_epoch_type":	"Treatment X"
        },
        {
            "key": "EPO009",
            "study_epoch_desc":	"Follow-up",
            "study_epoch_name":	"FOLLOW-UP",
            "study_epoch_type":	"Follow-up"
        }
    ],
    "STUDY_ELEMENT": [
        {
            "key": "EL004",
            "study_element_desc": "Screening",
            "study_element_name": "SCREENING",
        },
        {
            "key": "EL005",
            "study_element_desc": "AZD6738 + Durvalumab",
            "study_element_name": "AZD_DRUV",
        },
        {
            "key": "EL006",
            "study_element_desc": "AZD6738 + Olaparib",
            "study_element_name": "AZD_OLA",
        },
        {
            "key": "EL007",
            "study_element_desc": "Follow-up",
            "study_element_name": "FOLLOW-UP",
        }
    ],

    "RULE": [
        {
            "key": "RULE1",
            "rule_desc": "6 weeks prior to start treatment"
        },
        {
            "key": "RULE2",
            "rule_desc": "Start of treatment"
        },
        {
            "key": "RULE3",
            "rule_desc": "Start of treatment"
        },
        {
            "key": "RULE4",
            "rule_desc": "End of last treatment day"
        },
        {
            "key": "RULE5",
            "rule_desc": "Start of treatment",
        },
        {
            "key": "RULE6",
            "rule_desc": "End of last treatment day",
        },
        {
            "key": "RULE7",
            "rule_desc": "End of last treatment day",
        },
        {
            "key": "RULE8",
            "rule_desc": "Last follow-up measurement",
        }
    ],
    "STUDY_CELL": [
        {
            "key": "CEL004"
        },
        {
            "key": "CEL005"
        },
        {
            "key": "CEL006"
        },
        {
            "key": "CEL007"
        },
        {
            "key": "CEL008"
        },
        {
            "key": "CEL009"
        },
        {
            "key": "CEL010"
        },
        {
            "key": "CEL011"
        },
        {
            "key": "CEL012"
        },
        {
            "key": "CEL013"
        },
        {
            "key": "CEL014"
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
        {"from": "SD_1", "to": "CEL004"},
        {"from": "SD_1", "to": "CEL005"},
        {"from": "SD_1", "to": "CEL006"},
        {"from": "SD_1", "to": "CEL007"},
        {"from": "SD_1", "to": "CEL008"},
        {"from": "SD_1", "to": "CEL009"},
        {"from": "SD_1", "to": "CEL010"},
        {"from": "SD_1", "to": "CEL011"},
        {"from": "SD_1", "to": "CEL012"},
        {"from": "SD_1", "to": "CEL013"},
        {"from": "SD_1", "to": "CEL014"}
    ],
    "HAS_ARM": [
        { "from": "CEL004", "to": "ARM02" },
        { "from": "CEL005", "to": "ARM03" },
        { "from": "CEL006", "to": "ARM02" },
        { "from": "CEL007", "to": "ARM03" },
        { "from": "CEL008", "to": "ARM02" },
        { "from": "CEL009", "to": "ARM03" },
        { "from": "CEL010", "to": "ARM02" },
        { "from": "CEL011", "to": "ARM02" },
        { "from": "CEL012", "to": "ARM03" },
        { "from": "CEL013", "to": "ARM02" },
        { "from": "CEL014", "to": "ARM03" },
    ],
    "HAS_EPOCH": [
        { "from": "CEL004", "to": "EPO004" },
        { "from": "CEL005", "to": "EPO004" },
        { "from": "CEL006", "to": "EPO005" },
        { "from": "CEL007", "to": "EPO005" },
        { "from": "CEL008", "to": "EPO006" },
        { "from": "CEL009", "to": "EPO005" },
        { "from": "CEL010", "to": "EPO007" },
        { "from": "CEL011", "to": "EPO008" },
        { "from": "CEL012", "to": "EPO008" },
        { "from": "CEL013", "to": "EPO009" },
        { "from": "CEL014", "to": "EPO009" },
    ],
    "HAS_ELEMENT": [
        { "from": "CEL004", "to": "EL004" },
        { "from": "CEL005", "to": "EL004" },
        { "from": "CEL006", "to": "EL005" },
        { "from": "CEL007", "to": "EL006" },
        { "from": "CEL008", "to": "EL005" },
        { "from": "CEL009", "to": "EL006" },
        { "from": "CEL010", "to": "EL005" },
        { "from": "CEL011", "to": "EL005" },
        { "from": "CEL012", "to": "EL006" },
        { "from": "CEL013", "to": "EL007" },
        { "from": "CEL014", "to": "EL007" },
    ],
    "HAS_START_RULE": [
        { "from": "EL004", "to": "RULE1" },
        { "from": "EL005", "to": "RULE2" },
        { "from": "EL005", "to": "RULE3" },
        { "from": "EL006", "to": "RULE4" }
    ],
    "HAS_END_RULE": [
        { "from": "EL004", "to": "RULE5" },
        { "from": "EL005", "to": "RULE6" },
        { "from": "EL005", "to": "RULE7" },
        { "from": "EL006", "to": "RULE8" }
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


