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
            "key": "OBJ001",
            "objective_desc": "To assess the safety of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients"
        },
        {
            "key": "OBJ002",
            "objective_desc": "To assess the effect of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients who have failed to 1st-line chemotherapy and are in second phase of disease"
        },
        {
            "key": "OBJ003",
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
            "study_epoch_type":	"Screening",
            "sequence_in_study": 1
        },
        {
            "key": "EPO005",
            "study_epoch_desc":	"Run-In",
            "study_epoch_name":	"RUN-IN",
            "study_epoch_type":	"Run-IN",
            "sequence_in_study": 2
        },
        {
            "key": "EPO006",
            "study_epoch_desc":	"Treatment Cycle 1",
            "study_epoch_name":	"TREATMENT",
            "study_epoch_type":	"Treatment 1",
            "sequence_in_study": 3
        },
        {
            "key": "EPO007",
            "study_epoch_desc":	"Treatment Cycle 2",
            "study_epoch_name":	"TREATMENT",
            "study_epoch_type":	"Treatment 2",
            "sequence_in_study": 4
        },
        {
            "key": "EPO008",
            "study_epoch_desc":	"Following Cycles",
            "study_epoch_name":	"TREATMENT",
            "study_epoch_type":	"Treatment X",
            "sequence_in_study": 5
        },
        {
            "key": "EPO009",
            "study_epoch_desc":	"Follow-up",
            "study_epoch_name":	"FOLLOW-UP",
            "study_epoch_type":	"Follow-up",
            "sequence_in_study": 6
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
    ],
    "VISIT": [
        {    
            "key": "VIS11",
            "number": "001",
            "name": "SCREENING VISIT"
        },
        {   
            "key": "VIS12",
            "number": "002",
            "name": "RUN-IN VISIT 1"
        },
        {   
            "key": "VIS13",
            "number": "003",
            "name": "RUN-IN VISIT 2"
        },
        {   
            "key": "VIS14",
            "number": "004",
            "name": "RUN-IN VISIT 3"
        },
        {   
            "key": "VIS15",
            "number": "005",
            "name": "CYCLE 1, TREATMENT DAY 1"
        },
        {   
            "key": "VIS16",
            "number": "006",
            "name": "CYCLE 1, TREATMENT DAY 3"
        },
        {   
            "key": "VIS17",
            "number": "007",
            "name": "CYCLE 1, TREATMENT DAY 5"
        },
        {   
            "key": "VIS18",
            "number": "008",
            "name": "CYCLE 2, TREATMENT DAY 1"
        },
        {   
            "key": "VIS19",
            "number": "009",
            "name": "CYCLE 2, TREATMENT DAY 3"
        },
        {   
            "key": "VIS20",
            "number": "010",
            "name": "CYCLE X, TREATMENT DAY 1"
        },
        {   
            "key": "VIS21",
            "number": "011",
            "name": "CYCLE X, TREATMENT DAY 4"
        },
        {   
            "key": "VIS22",
            "number": "012",
            "name": "FU 1"
        },
        {   
            "key": "VIS23",
            "number": "013",
            "name": "FU 2"
        }
    ],
    #start_rule_id uuid,
    #end_rule_id uuid,
    #contact_mode_id integer,
    #env_setting_id integer,
    #encounter_type_id integer,
    #first_activity_id uuid,
    "WORKFLOW_ITEM": [
        {   
            "key": "WF011", 
            "description": "Informed Consent"
        },
        {   
            "key": "WF012", 
            "description": "Hematology"
        },
        {   
            "key": "WF013", 
            "description": "Biochemsitry"
        },
        {   
            "key": "WF014", 
            "description": "Serology"
        },
        {   
            "key": "WF015", 
            "description": "Urinalysis"
        },
        {   
            "key": "WF016", 
            "description": "Pregnancy test"
        },
        {   
            "key": "WF017", 
            "description": "Brolucizumab administration"
        },
        {   
            "key": "WF018", 
            "description": "Concomitant medication"
        }
    ],
    #from_point_in_time uuid NOT NULL,
    #to_point_in_time uuid NOT NULL,
    #worklfow_matrix_id uuid NOT NULL,
    "ACTIVITY": [
        {   
            "key": "ACT001"
        },
        {   
            "key": "ACT002"
        },
        {   
            "key": "ACT003"
        }
    ],
    "PROCEDURE": [
        {   
            "key": "PROC001",
            "description": "Remote ICF collection"
        },
        {   
            "key": "PROC002",
            "description": "Blood sample collection"
        },
        {   
            "key": "PROC003",
            "description": "Blood sample analysis"
        }   
    ],
    "STUDY_DATA": [
        {   
            "key": "SD001",
            "name": "ALAT",
            "description": "",
            "ecrf_link": ""
        },
        {   
            "key": "SD002",
            "name": "ASAT",
            "description": "",
            "ecrf_link": ""
        },
        {   
            "key": "SD003",
            "name": "ERY",
            "description": "",
            "ecrf_link": ""
        },
        {   
            "key": "SD004",
            "name": "WBC",
            "description": "",
            "ecrf_link": ""
        }   
    ],
    "ENDPOINT": [
        {
            "key": "E001", 
            "endpoint_desc": "Disease control rate of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "PRIMARY",
            "endpoint_purpose": "EFFICACY",
        },
        {
            "key": "E002", 
            "endpoint_desc": "Disease control rate of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "PRIMARY",
            "endpoint_purpose": "EFFICACY",
        },
        {
            "key": "E003", 
            "endpoint_desc": "Overall response rate of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY",
        },
        {
            "key": "E004", 
            "endpoint_desc": "progression-free survival of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY",
        },
        {
            "key": "E005", 
            "endpoint_desc": "duration of response of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "PHARMACODYNAMIC"
        },
        {
            "key": "E006", 
            "endpoint_desc": "overall survival of response of AZD6738 + Durvalumab cohort [ Time Frame: every 12 weeks until death or up to 5 years ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY"
        },
        {
            "key": "E007", 
            "endpoint_desc": "Safety and tolerability of AZD6738 + Durvalumab cohort measured by number and grade of toxicity events [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "SAFETY"
        },
        {
            "key": "E008", 
            "endpoint_desc": "quality of life measurement of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY"
        },
        {
            "key": "E009", 
            "endpoint_desc": "overall response rate (ORR) of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY"
        },
        {
            "key": "E010", 
            "endpoint_desc": "progression-free survival of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY",
        },
        {
            "key": "E011", 
            "endpoint_desc": "duration of response of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "PHARMACODYNAMIC"
        },
        {
            "key": "E012", 
            "endpoint_desc": "overall survival of AZD6738 + Olaparib cohort [ Time Frame: every 12 weeks until death or up to 5 years ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY"
        },
        {
            "key": "E013", 
            "endpoint_desc": "Safety and tolerability of AZD6738 + Olaparib cohort as measured by number and grade of toxicity events [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "SAFETY"
        },
        {
            "key": "E014", 
            "endpoint_desc": "quality of life measurement of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
            "outcome_level": "SECONDARY",
            "endpoint_purpose": "EFFICACY"
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
        {"from": "SD_1", "to": "OBJ001"},
        {"from": "SD_1", "to": "OBJ002"},
        {"from": "SD_1", "to": "OBJ003"},
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
    ],
    "HAS_VISIT": [
        { "to": "VIS11", "from": "EPO004" },
        { "to": "VIS12", "from": "EPO005" },
        { "to": "VIS13", "from": "EPO005" },
        { "to": "VIS14", "from": "EPO005" },
        { "to": "VIS15", "from": "EPO006" },
        { "to": "VIS16", "from": "EPO006" },
        { "to": "VIS17", "from": "EPO006" },
        { "to": "VIS18", "from": "EPO007" },
        { "to": "VIS19", "from": "EPO007" },
        { "to": "VIS20", "from": "EPO008" },
        { "to": "VIS21", "from": "EPO008" },
        { "to": "VIS22", "from": "EPO009" },
        { "to": "VIS23", "from": "EPO009" }
    ], 
    "HAS_ACTIVITY": [
        {"from": "WF011", "to": "ACT001" },
        {"from": "WF012", "to": "ACT003" },
        {"from": "WF013", "to": "ACT002" }
    ],
# Workflow to Arm      
#WF011 ARM03   
#WF012 ARM03   
#WF013 ARM03   
#WF014 ARM03   
#WF015 ARM03   
#WF016 ARM03   
#WF017 ARM03   
#WF018 ARM03   
      
    "HAS_ENCOUNTER": [
        {"from": "WF011", "to": "VIS11" },
        {"from": "WF012", "to": "VIS11" },
        {"from": "WF012", "to": "VIS12" },
        {"from": "WF012", "to": "VIS14" },
        {"from": "WF012", "to": "VIS15" },
        {"from": "WF012", "to": "VIS18" },
        {"from": "WF012", "to": "VIS20" },
        {"from": "WF012", "to": "VIS22" },
        {"from": "WF012", "to": "VIS23" },
        {"from": "WF013", "to": "VIS11" },
        {"from": "WF013", "to": "VIS12" },
        {"from": "WF013", "to": "VIS14" },
        {"from": "WF013", "to": "VIS15" },
        {"from": "WF013", "to": "VIS18" },
        {"from": "WF013", "to": "VIS20" },
        {"from": "WF013", "to": "VIS22" },
        {"from": "WF013", "to": "VIS23" },
        {"from": "WF014", "to": "VIS11" },
        {"from": "WF014", "to": "VIS14" },
        {"from": "WF014", "to": "VIS15" },
        {"from": "WF014", "to": "VIS18" },
        {"from": "WF014", "to": "VIS20" },
        {"from": "WF014", "to": "VIS22" },
        {"from": "WF014", "to": "VIS23" },
        {"from": "WF015", "to": "VIS11" },
        {"from": "WF015", "to": "VIS15" },
        {"from": "WF015", "to": "VIS22" },
        {"from": "WF016", "to": "VIS11" },
        {"from": "WF016", "to": "VIS22" },
        {"from": "WF017", "to": "VIS15" },
        {"from": "WF017", "to": "VIS18" },
        {"from": "WF017", "to": "VIS20" },
        {"from": "WF018", "to": "VIS11" },
        {"from": "WF018", "to": "VIS15" },
        {"from": "WF018", "to": "VIS18" },
        {"from": "WF018", "to": "VIS20" },
        {"from": "WF018", "to": "VIS22" }
    ],
    "HAS_PREVIOUS_WORKFLOW": [
        {"from": "WF012", "to": "WF011" },
        {"from": "WF013", "to": "WF012" },
        {"from": "WF014", "to": "WF013" },
        {"from": "WF015", "to": "WF014" },
        {"from": "WF016", "to": "WF015" },
        {"from": "WF017", "to": "WF016" },
        {"from": "WF018", "to": "WF017" }
    ],
    "HAS_PROCEDURE": [
        {"from": "ACT001", "to": "PROC001" },
        {"from": "ACT002", "to": "PROC002" },
        {"from": "ACT002", "to": "PROC003" },
        {"from": "ACT003", "to": "PROC002" },
        {"from": "ACT003", "to": "PROC003" }
    ],
    "HAS_STUDY_DATA": [
        {"from": "ACT002", "to": "SD001" },
        {"from": "ACT002", "to": "SD002" },
        {"from": "ACT003", "to": "SD003" },
        {"from": "ACT003", "to": "SD004" }
    ],
    "HAS_ENDPOINT": [
        {"from": "OBJ001", "to": "E001" },
        {"from": "OBJ001", "to": "E002" },
        {"from": "OBJ001", "to": "E003" },
        {"from": "OBJ001", "to": "E004" },
        {"from": "OBJ001", "to": "E005" },
        {"from": "OBJ001", "to": "E006" },
        {"from": "OBJ001", "to": "E008" },
        {"from": "OBJ001", "to": "E009" },
        {"from": "OBJ001", "to": "E010" },
        {"from": "OBJ001", "to": "E011" },
        {"from": "OBJ001", "to": "E012" },
        {"from": "OBJ001", "to": "E014" },
        {"from": "OBJ002", "to": "E007" },
        {"from": "OBJ002", "to": "E013" },
        {"from": "OBJ003", "to": "E001" },
        {"from": "OBJ003", "to": "E002" },
        {"from": "OBJ003", "to": "E003" },
        {"from": "OBJ003", "to": "E004" },
        {"from": "OBJ003", "to": "E005" },
        {"from": "OBJ003", "to": "E006" },
        {"from": "OBJ003", "to": "E008" },
        {"from": "OBJ003", "to": "E009" },
        {"from": "OBJ003", "to": "E010" },
        {"from": "OBJ003", "to": "E011" },
        {"from": "OBJ003", "to": "E012" },
        {"from": "OBJ003", "to": "E014" }
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


