# Program to inject a DDF study design into Neo4j

from neo4j import GraphDatabase

the_nodes = {
    "STUDY": [
        {
            "key": "S_1",
            "study_title": "Umbrella Study of DDR (DNA-Damage Response) Targeting Agents in Advanced Biliary Tract Cancer",
            "study_version": "???",
            "study_tag": "???",
            "study_status": "???"
        },
        {
            "key": "XXX3",
            "study_title": "Real-world Evaluation of Brolucizumab for the Treatment of Neovascular (Wet) Age-related Macular Degeneration (AMD) (IRIS Study)",
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
        },
    	{
            "key": "PR04",
            "brief_title": "RW evaluation of treatment with Brolucizumab", 
            "official_title": "Real-world Evaluation of Brolucizumab for the Treatment of Neovascular (Wet) Age-related Macular Degeneration (AMD) (IRIS Study)",
            "PublicTitle": "",
            "scientific_title": "",
            "amendments": ""
        }
    ],
    "INDICATION": [
        {
            "key": "TI01",
            "indication_desc": "Bile duct cancer"
        },
        {
            "key": "TI02",
            "indication_desc": "Influenza"
        }
    ],
    "STUDY_DESIGN": [
        {
            "key": "SD_1"
        }
    ],
    "POPULATION": [
        {
            "key": "P001",
            "population_desc": "biliary tract cancer patients who have failed to 1st-line chemotherapy"
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
            "key": "CD001",
            "code": "24662006",
            "code_system": "SNOMED-CT",
            "code_system_version": "4.0.6.4",
            "decode": "Influenza due to Influenza virus, type B"
        },
        {
            "key": "CD002",
            "code": "1022000",
            "code_system": "MEDDRA",
            "code_system_version": "Nov18_2021",
            "decode": "Influenza"
        },
        {
            "key": "CD003",
            "code": "J11.1",
            "code_system": "ICD	10",
            "code_system_version": "",
            "decode": "Influenza due to unidentified influenza virus with other respiratory manifestations"
        },
        {
            "key": "CD004",
            "code": "C22.1",
            "code_system": "ICD	10",
            "code_system_version": "",
            "decode": "Intrahepatic bile duct carcinoma"
        },
        {
            "key": "CD005",
            "code": "371970002",
            "code_system": "SNOMED-CT",
            "code_system_version": "4.0.6.4",
            "decode": "Primary malignant neoplasm of biliary tract (disorder)"
        },
        {
            "key": "CD006",
            "code": "10004596",
            "code_system": "MEDDRA",
            "code_system_version": "Nov18_2021",
            "decode": "Bile duct cancer recurrent"
        },
        {
            "key": "CD007",
            "code": "J07BX03",
            "code_system": "ATC	2020",
            "code_system_version": "",
            "decode": "Covid-19 vaccines"
        },
        {
            "key": "CD008",
            "code": "L01XC28",
            "code_system": "ATC",
            "code_system_version": "14-12-2021",
            "decode": "Durvalumab"
        },
        {
            "key": "CD009",
            "code": "L01XK01",
            "code_system": "ATC",
            "code_system_version": "14-12-2021",
            "decode": "Olaparib"
        },
        {
            "key": "CD010",
            "code": "249565666",
            "code_system": "PubChem",
            "code_system_version": "09/02/2021",
            "decode": "Durvalumab; Imfinzi; Anti-B7H1; Monoclonal Antibody"
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
        },
        {
            "key": "RULE09",
            "rule_desc": "-D5"
        },
        {
            "key": "RULE10",
            "rule_desc": "-D3"
        },
        {
            "key": "RULE11",
            "rule_desc": "-D1"
        },
        {
            "key": "RULE12",
            "rule_desc": "D1"
        },
        {
            "key": "RULE13",
            "rule_desc": "D3"
        },
        {
            "key": "RULE14",
            "rule_desc": "D5"
        },
        {
            "key": "RULE15",
            "rule_desc": "D1"
        },
        {
            "key": "RULE16",
            "rule_desc": "D3"
        },
        {
            "key": "RULE17",
            "rule_desc": "D1"
        },
        {
            "key": "RULE18",
            "rule_desc": "D4"
        },
        {
            "key": "RULE19",
            "rule_desc": "W2"
        },
        {
            "key": "RULE20",
            "rule_desc": "W4"
        },
        {
            "key": "RULE21",
            "rule_desc": "-D5"
        },
        {
            "key": "RULE22",
            "rule_desc": "-D3"
        },
        {
            "key": "RULE23",
            "rule_desc": "-D1"
        },
        {
            "key": "RULE24",
            "rule_desc": "D1"
        },
        {
            "key": "RULE25",
            "rule_desc": "D3"
        },
        {
            "key": "RULE26",
            "rule_desc": "D5"
        },
        {
            "key": "RULE27",
            "rule_desc": "D1"
        },
        {
            "key": "RULE28",
            "rule_desc": "D3"
        },
        {
            "key": "RULE29",
            "rule_desc": "D1"
        },
        {
            "key": "RULE30",
            "rule_desc": "D4"
        },
        {
            "key": "RULE31",
            "rule_desc": "W2"
        },
        {
            "key": "RULE32",
            "rule_desc": "W4"
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
            "name": "SCREENING VISIT",
            "contact_mode": "IN PERSON",
            "env_setting": "CLINIC",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS12",
            "number": "002",
            "name": "RUN-IN VISIT 1",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS13",
            "number": "003",
            "name": "RUN-IN VISIT 2",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS14",
            "number": "004",
            "name": "RUN-IN VISIT 3",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS15",
            "number": "005",
            "name": "CYCLE 1, TREATMENT DAY 1",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS16",
            "number": "006",
            "name": "CYCLE 1, TREATMENT DAY 3",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS17",
            "number": "007",
            "name": "CYCLE 1, TREATMENT DAY 5",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS18",
            "number": "008",
            "name": "CYCLE 2, TREATMENT DAY 1",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS19",
            "number": "009",
            "name": "CYCLE 2, TREATMENT DAY 3",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS20",
            "number": "010",
            "name": "CYCLE X, TREATMENT DAY 1",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS21",
            "number": "011",
            "name": "CYCLE X, TREATMENT DAY 4",
            "contact_mode": "IN PERSON",
            "env_setting": "HOSPITAL",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS22",
            "number": "012",
            "name": "FU 1",
            "contact_mode": "IN PERSON",
            "env_setting": "CLINIC",
            "encounter_type": "PLANNED VISIT"
        },
        {   
            "key": "VIS23",
            "number": "013",
            "name": "FU 2",
            "contact_mode": "REMOTE AUDIO",
            "encounter_type": "VIRTUAL VISIT"
        }
    ],
    #start_rule_id uuid,
    #end_rule_id uuid,
    #first_activity_id uuid,
    
    "WORKFLOW_ITEM": [
        { "key": "WF001" },
        { "key": "WF002" },
        { "key": "WF003" },
        { "key": "WF004" },
        { "key": "WF005" },
        { "key": "WF006" },
        { "key": "WF007" },
        { "key": "WF008" },
        { "key": "WF009" },
        { "key": "WF010" },
        { "key": "WF011" },
        { "key": "WF012" },
        { "key": "WF013" },
        { "key": "WF014" },
        { "key": "WF015" },
        { "key": "WF016" },
        { "key": "WF017" },
        { "key": "WF018" },
        { "key": "WF019" },
        { "key": "WF020" },
        { "key": "WF021" },
        { "key": "WF022" },
        { "key": "WF023" },
        { "key": "WF024" },
        { "key": "WF025" },
        { "key": "WF026" },
        { "key": "WF027" },
        { "key": "WF028" },
        { "key": "WF029" },
        { "key": "WF030" },
        { "key": "WF031" },
        { "key": "WF032" },
        { "key": "WF033" },
        { "key": "WF034" },
        { "key": "WF035" },
        { "key": "WF036" },
        { "key": "WF037" },
        { "key": "WF038" },
        { "key": "WF039" },
        { "key": "WF040" },
        { "key": "WF041" },
        { "key": "WF042" },
        { "key": "WF043" },
        { "key": "WF044" },
        { "key": "WF045" },
        { "key": "WF046" },
        { "key": "WF047" },
        { "key": "WF048" },
        { "key": "WF049" },
        { "key": "WF050" },
        { "key": "WF051" },
        { "key": "WF052" },
        { "key": "WF053" },
        { "key": "WF054" },
        { "key": "WF055" },
        { "key": "WF056" }
    ],
    #from_point_in_time uuid NOT NULL,
    #to_point_in_time uuid NOT NULL,
    #worklfow_matrix_id uuid NOT NULL,
    "ACTIVITY": [
        {   
            "key": "ACT001",
            "description": "Informed consent"
        },
        {   
            "key": "ACT002",
            "description": "Eligibility criteria"
        },		
        {   
            "key": "ACT003",
            "description": "Demography"
        },
        {   
            "key": "ACT004",
            "description": "Medical history"
        },	
        {   
            "key": "ACT005",
            "description": "Disease characteristics"
        },
        {   
            "key": "ACT006",
            "description": "Physical exam"
        },		
        {   
            "key": "ACT007",
            "description": "Height"
        },
        {   
            "key": "ACT008",
            "description": "12-lead ECG"
        },
        {   
            "key": "ACT009",
            "description": "Hematology (predose)"
        },
        {   
            "key": "ACT010",
            "description": "Chemistry (predose)"
        },
        {   
            "key": "ACT011",
            "description": "Serology"
        },	
        {   
            "key": "ACT012",
            "description": "Urinalysis"
        },
        {   
            "key": "ACT013",
            "description": "Pregnancy test"
        },
        {   
            "key": "ACT014",
            "description": "Ensure availability of medication X"
        },
        {   
            "key": "ACT015",
            "description": "Hospitalization"
        },
        {   
            "key": "ACT016",
            "description": "Weight"
        },
        {   
            "key": "ACT017",
            "description": "Vital signs"
        },
        {   
            "key": "ACT018",
            "description": "adverse events"
        },
        {   
            "key": "ACT019",
            "description": "Concomitant medications"
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
        },
        {   
            "key": "PROC004",
            "description": "Drug administration"
        },
        {   
            "key": "PROC005",
            "description": "Hospitalisation"
        },
        {   
            "key": "PROC006",
            "description": "Weight measurement"
        }
    ],
    "STUDY_DATA": [
        {   
            "key": "SD001",
            "name": "ALAT",
            "description": "",
            "ecrf_link": "https://www.dropbox.com/s/84quxhfj254k2sh/LB_LOCAL_XML.xml?dl=1"
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
            "description": "Erythrocytes",
            "ecrf_link": ""
        },   
        {   
            "key": "SD004",
            "name": "WBC",
            "description": "White blood cell count",
            "ecrf_link": ""
        },  
        {   
            "key": "SD005",
            "name": "DOSDATE",
            "description": "Date of investigational drug administration",
            "ecrf_link": ""
        },   
        {   
            "key": "SD006",
            "name": "WGHT",
            "description": "Weight",
            "ecrf_link": ""
        },   
        {   
            "key": "SD007",
            "name": "AGE",
            "description": "Age",
            "ecrf_link": ""
        },   
        {   
            "key": "SD008",
            "name": "OAS",
            "description": "Oncology Assessment Scale",
            "ecrf_link": ""
        },   
        {   
            "key": "SD009",
            "name": "DPS",
            "description": "Disease Progression Scale",
            "ecrf_link": ""
        },   
        {   
            "key": "SD010",
            "name": "TSO",
            "description": "Time since onset",
            "ecrf_link": ""
        },   
        {   
            "key": "SD011",
            "name": "HGT",
            "description": "Height",
            "ecrf_link": ""
        },   
        {   
            "key": "SD012",
            "name": "QTc",
            "description": "QTc interval",
            "ecrf_link": ""
        },   
        {   
            "key": "SD013",
            "name": "ST",
            "description": "St-segment",
            "ecrf_link": ""
        },   
        {   
            "key": "SD014",
            "name": "WBC_DIP",
            "description": "WBC dipstick",
            "ecrf_link": ""
        },   
        {   
            "key": "SD015",
            "name": "HCG",
            "description": "Serum HCG",
            "ecrf_link": ""
        },   
        {   
            "key": "SD016",
            "name": "SBP",
            "description": "Systolic blood pressure",
            "ecrf_link": ""
        },   
        {   
            "key": "SD017",
            "name": "DBP",
            "description": "Diastolic Blood Pressure",
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
        {"from": "XXX3", "to": "PR04"}
    ],
    "HAS_STUDY_DESIGN": [
        {"from": "S_1", "to": "SD_1"},
    ],
    "HAS_POPULATION": [
        {"from": "SD_1", "to": "P001" }
    ],
    "HAS_INVESTIGATIONAL_INTERVENTION": [
        {"from": "SD_1", "to": "II_1"},
        {"from": "SD_1", "to": "II_2"},
        {"from": "SD_1", "to": "II_3"},
    ],
    "HAS_INDICATION": [
        {"from": "SD_1", "to": "TI01"},
        {"from": "SD_1", "to": "TI02"}
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
        { "from": "EL006", "to": "RULE4" },
        { "from": "VIS12", "to": "RULE09" },
        { "from": "VIS13", "to": "RULE10" },
        { "from": "VIS14", "to": "RULE11" },
        { "from": "VIS15", "to": "RULE12" },
        { "from": "VIS16", "to": "RULE13" },
        { "from": "VIS17", "to": "RULE14" },
        { "from": "VIS18", "to": "RULE15" },
        { "from": "VIS19", "to": "RULE16" },
        { "from": "VIS20", "to": "RULE17" },
        { "from": "VIS21", "to": "RULE18" },
        { "from": "VIS22", "to": "RULE19" },
        { "from": "VIS23", "to": "RULE20" }
    ],
    "HAS_END_RULE": [
        { "from": "EL004", "to": "RULE5" },
        { "from": "EL005", "to": "RULE6" },
        { "from": "EL005", "to": "RULE7" },
        { "from": "EL006", "to": "RULE8" },
        { "from": "VIS12", "to": "RULE21" },
        { "from": "VIS13", "to": "RULE22" },
        { "from": "VIS14", "to": "RULE23" },
        { "from": "VIS15", "to": "RULE24" },
        { "from": "VIS16", "to": "RULE25" },
        { "from": "VIS17", "to": "RULE26" },
        { "from": "VIS18", "to": "RULE27" },
        { "from": "VIS19", "to": "RULE28" },
        { "from": "VIS20", "to": "RULE29" },
        { "from": "VIS21", "to": "RULE30" },
        { "from": "VIS22", "to": "RULE31" },
        { "from": "VIS23", "to": "RULE32" }
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
        { "from": "WF001", "to": "ACT001" },
        { "from": "WF002", "to": "ACT002" },
        { "from": "WF003", "to": "ACT003" },
        { "from": "WF004", "to": "ACT004" },
        { "from": "WF005", "to": "ACT005" },
        { "from": "WF006", "to": "ACT006" },
        { "from": "WF007", "to": "ACT006" },
        { "from": "WF008", "to": "ACT006" },
        { "from": "WF009", "to": "ACT007" },
        { "from": "WF010", "to": "ACT008" },
        { "from": "WF011", "to": "ACT008" },
        { "from": "WF012", "to": "ACT008" },
        { "from": "WF013", "to": "ACT008" },
        { "from": "WF014", "to": "ACT008" },
        { "from": "WF015", "to": "ACT009" },
        { "from": "WF016", "to": "ACT009" },
        { "from": "WF017", "to": "ACT009" },
        { "from": "WF018", "to": "ACT010" },
        { "from": "WF019", "to": "ACT010" },
        { "from": "WF020", "to": "ACT010" },
        { "from": "WF021", "to": "ACT011" },
        { "from": "WF022", "to": "ACT011" },
        { "from": "WF023", "to": "ACT011" },
        { "from": "WF024", "to": "ACT011" },
        { "from": "WF025", "to": "ACT011" },
        { "from": "WF026", "to": "ACT011" },
        { "from": "WF027", "to": "ACT011" },
        { "from": "WF028", "to": "ACT011" },
        { "from": "WF029", "to": "ACT012" },
        { "from": "WF030", "to": "ACT012" },
        { "from": "WF031", "to": "ACT012" },
        { "from": "WF032", "to": "ACT013" },
        { "from": "WF033", "to": "ACT013" },
        { "from": "WF034", "to": "ACT014" },
        { "from": "WF035", "to": "ACT014" },
        { "from": "WF036", "to": "ACT014" },
        { "from": "WF037", "to": "ACT015" },
        { "from": "WF038", "to": "ACT015" },
        { "from": "WF039", "to": "ACT015" },
        { "from": "WF040", "to": "ACT015" },
        { "from": "WF041", "to": "ACT016" },
        { "from": "WF042", "to": "ACT016" },
        { "from": "WF043", "to": "ACT016" },
        { "from": "WF044", "to": "ACT016" },
        { "from": "WF045", "to": "ACT017" },
        { "from": "WF046", "to": "ACT017" },
        { "from": "WF047", "to": "ACT017" },
        { "from": "WF048", "to": "ACT017" },
        { "from": "WF049", "to": "ACT017" },
        { "from": "WF050", "to": "ACT017" },
        { "from": "WF051", "to": "ACT017" },
        { "from": "WF052", "to": "ACT017" },
        { "from": "WF053", "to": "ACT017" },
        { "from": "WF054", "to": "ACT017" },
        { "from": "WF055", "to": "ACT017" },
        { "from": "WF056", "to": "ACT017" }
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
      
    "USED_IN_VISIT": [
        { "from": "WF001", "to": "VIS11" },
        { "from": "WF002", "to": "VIS11" },
        { "from": "WF003", "to": "VIS11" },
        { "from": "WF004", "to": "VIS11" },
        { "from": "WF005", "to": "VIS11" },
        { "from": "WF006", "to": "VIS11" },
        { "from": "WF007", "to": "VIS13" },
        { "from": "WF008", "to": "VIS22" },
        { "from": "WF009", "to": "VIS11" },
        { "from": "WF010", "to": "VIS11" },
        { "from": "WF011", "to": "VIS12" },
        { "from": "WF012", "to": "VIS13" },
        { "from": "WF013", "to": "VIS14" },
        { "from": "WF014", "to": "VIS22" },
        { "from": "WF015", "to": "VIS11" },
        { "from": "WF016", "to": "VIS14" },
        { "from": "WF017", "to": "VIS22" },
        { "from": "WF018", "to": "VIS11" },
        { "from": "WF019", "to": "VIS14" },
        { "from": "WF020", "to": "VIS22" },
        { "from": "WF021", "to": "VIS11" },
        { "from": "WF022", "to": "VIS12" },
        { "from": "WF023", "to": "VIS13" },
        { "from": "WF024", "to": "VIS14" },
        { "from": "WF025", "to": "VIS15" },
        { "from": "WF026", "to": "VIS18" },
        { "from": "WF027", "to": "VIS20" },
        { "from": "WF028", "to": "VIS22" },
        { "from": "WF029", "to": "VIS11" },
        { "from": "WF030", "to": "VIS14" },
        { "from": "WF031", "to": "VIS22" },
        { "from": "WF032", "to": "VIS11" },
        { "from": "WF033", "to": "VIS14" },
        { "from": "WF034", "to": "VIS15" },
        { "from": "WF035", "to": "VIS18" },
        { "from": "WF036", "to": "VIS20" },
        { "from": "WF037", "to": "VIS12" },
        { "from": "WF038", "to": "VIS15" },
        { "from": "WF039", "to": "VIS18" },
        { "from": "WF040", "to": "VIS20" },
        { "from": "WF041", "to": "VIS01" },
        { "from": "WF042", "to": "VIS15" },
        { "from": "WF043", "to": "VIS18" },
        { "from": "WF044", "to": "VIS22" },
        { "from": "WF045", "to": "VIS11" },
        { "from": "WF046", "to": "VIS12" },
        { "from": "WF047", "to": "VIS13" },
        { "from": "WF048", "to": "VIS14" },
        { "from": "WF049", "to": "VIS15" },
        { "from": "WF050", "to": "VIS16" },
        { "from": "WF051", "to": "VIS17" },
        { "from": "WF052", "to": "VIS18" },
        { "from": "WF053", "to": "VIS19" },
        { "from": "WF054", "to": "VIS20" },
        { "from": "WF055", "to": "VIS21" },
        { "from": "WF056", "to": "VIS22" }
    ],
    "HAS_PREVIOUS_WORKFLOW": [
    ],
    "HAS_PREVIOUS_ACTIVITY": [
        { "from": "ACT002", "to": "ACT001" },
        { "from": "ACT003", "to": "ACT002" },
        { "from": "ACT004", "to": "ACT003" },
        { "from": "ACT005", "to": "ACT004" },
        { "from": "ACT006", "to": "ACT005" },
        { "from": "ACT007", "to": "ACT006" },
        { "from": "ACT008", "to": "ACT007" },
        { "from": "ACT009", "to": "ACT008" },
        { "from": "ACT010", "to": "ACT009" },
        { "from": "ACT011", "to": "ACT010" },
        { "from": "ACT012", "to": "ACT011" },
        { "from": "ACT013", "to": "ACT012" },
        { "from": "ACT014", "to": "ACT013" },
        { "from": "ACT015", "to": "ACT014" },
        { "from": "ACT016", "to": "ACT015" },
        { "from": "ACT017", "to": "ACT016" },
        { "from": "ACT018", "to": "ACT017" },
        { "from": "ACT019", "to": "ACT018" }
    ],
    "HAS_PROCEDURE": [
        { "from": "ACT001", "to": "PROC001" },
        { "from": "ACT009", "to": "PROC002" },
        { "from": "ACT009", "to": "PROC003" },
        { "from": "ACT010", "to": "PROC002" },
        { "from": "ACT010", "to": "PROC003" },
        { "from": "ACT015", "to": "PROC005" },
        { "from": "ACT016", "to": "PROC006" }
    ],
    "HAS_STUDY_DATA": [
        {"from": "ACT003", "to": "SD007" },
        {"from": "ACT005", "to": "SD008" },
        {"from": "ACT005", "to": "SD010" },
        {"from": "ACT005", "to": "SD010" },
        {"from": "ACT007", "to": "SD011" },
        {"from": "ACT008", "to": "SD012" },
        {"from": "ACT008", "to": "SD013" },
        {"from": "ACT009", "to": "SD003" },
        {"from": "ACT009", "to": "SD004" },
        {"from": "ACT010", "to": "SD001" },
        {"from": "ACT010", "to": "SD002" },
        {"from": "ACT012", "to": "SD014" },
        {"from": "ACT013", "to": "SD015" },
        {"from": "ACT014", "to": "SD005" },
        {"from": "ACT016", "to": "SD006" },
        {"from": "ACT017", "to": "SD016" },
        {"from": "ACT017", "to": "SD017" }
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
    ],
    "HAS_CODED": [
        {"from": "TI02", "to": "CD001" },
        {"from": "TI02", "to": "CD002" },
        {"from": "TI02", "to": "CD003" },
        {"from": "TI01", "to": "CD004" },
        {"from": "TI01", "to": "CD005" },
        {"from": "TI01", "to": "CD006" },
        {"from": "II_2", "to": "CD008" },
        {"from": "II_1", "to": "CD009" },
        {"from": "II_2", "to": "CD010" },
    ]
}

def clear(tx):
    tx.run("MATCH (n) DETACH DELETE n")

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
