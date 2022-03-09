# Code for generating simple Study CRF from the DDF activities list

from neo4j import GraphDatabase
from beautifultable import BeautifulTable
import urllib.request
import lxml.etree as ElementTree
import datetime

exported_at = datetime.datetime.now().replace(microsecond=0).isoformat()
odm_namespace = "http://www.cdisc.org/ns/odm/v1.3"
ElementTree.register_namespace('odm', odm_namespace)

def extract_form(xml_doc, study_event_def, form_name, the_forms, the_item_groups, the_items, the_code_lists, match=True):
    forms = None
    if match:
        print("    Matching Form")
        forms = xml_doc.findall(".//{http://www.cdisc.org/ns/odm/v1.3}FormDef[@Name='%s']" % (form_name))
    else:
        print("    Not Matching Form")
        forms = xml_doc.findall(".//{http://www.cdisc.org/ns/odm/v1.3}FormDef")
    if not forms:
        if not match:
            print(xml_doc)
        print("    Form: Missing")
        return None
    else:
        print("    Form:", forms[0])
    form = forms[0]
    the_forms.append(form)
    form_ref = ElementTree.SubElement(study_event_def, "FormRef")
    form_ref.set("FormOID", form.attrib["OID"])
    form_ref.set("Mandatory", "Yes")
    form_ref.set("OrderNumber", "1")

    item_group_refs = form.findall('{http://www.cdisc.org/ns/odm/v1.3}ItemGroupRef')
    for item_groupref in item_group_refs:
        oid = item_groupref.attrib['ItemGroupOID']
        item_groups = xml_doc.findall(".//{http://www.cdisc.org/ns/odm/v1.3}ItemGroupDef[@OID='%s']" % (oid)) 
        item_group = item_groups[0]
        the_item_groups.append(item_group)
        item_refs = item_group.findall('{http://www.cdisc.org/ns/odm/v1.3}ItemRef')
        for item_ref in item_refs:
            oid = item_ref.attrib['ItemOID']
            items = xml_doc.findall(".//{http://www.cdisc.org/ns/odm/v1.3}ItemDef[@OID='%s']" % (oid)) 
            item = items[0]
            the_items.append(item)
            code_list_refs = item.findall('{http://www.cdisc.org/ns/odm/v1.3}CodeListRef')
            for code_list_ref in code_list_refs:
                oid = code_list_ref.attrib['CodeListOID']
                code_lists = xml_doc.findall(".//{http://www.cdisc.org/ns/odm/v1.3}CodeList[@OID='%s']" % (oid)) 
                code_list = code_lists[0]
                the_code_lists.append(code_list)
            measurement_unit_refs = item.findall('{http://www.cdisc.org/ns/odm/v1.3}MeasurementUnitRef')
            for measurement_unit_ref in measurement_unit_refs:
                oid = measurement_unit_ref.attrib['MeasurementUnitOID']
                measurement_units = xml_doc.findall(".//{http://www.cdisc.org/ns/odm/v1.3}MeasurementUnit[@OID='%s']" % (oid)) 
                if measurement_units:
                    measurement_unit = measurement_units[0]
                    basic_definitions.append(measurement_unit)
    return form

def blank_form(study_event_def, form_name, the_forms, the_item_groups, the_items, the_code_lists):
    form = ElementTree.Element("{%s}FormDef" % (odm_namespace))
    form.set("OID", "DDF_F_%s" % (len(the_forms) + 1)) 
    form.set("Name", form_name) 
    form.set("Repeating", "No") 
    the_forms.append(form)
    form_ref = ElementTree.SubElement(study_event_def, "{%s}FormRef" % (odm_namespace))
    form_ref.set("FormOID", form.attrib["OID"])
    form_ref.set("Mandatory", "Yes")
    form_ref.set("OrderNumber", "1")
    item_group_ref = ElementTree.SubElement(form, "{%s}ItemGroupRef" % (odm_namespace))
    item_group_ref.set("ItemGroupOID", "DDF_F_%s_IG" % (len(the_forms) + 1)) 
    item_group_ref.set("OrderNumber", "1") 
    item_group = ElementTree.Element("{%s}ItemGroupDef" % (odm_namespace))
    item_group.set("OID", "DDF_F_%s_IG" % (len(the_forms) + 1)) 
    item_group.set("Name", form_name) 
    item_group.set("Repeating", "No")
    the_item_groups.append(item_group)
    item_ref = ElementTree.SubElement(item_group, "{%s}ItemRef" % (odm_namespace))
    item_ref.set("ItemOID", "DDF_F_%s_IG_I" % (len(the_forms) + 1)) 
    item_ref.set("Mandatory", "Yes")
    item_ref.set("OrderNumber", "1")
    item = ElementTree.Element("{%s}ItemDef" % (odm_namespace))
    item.set("OID", "DDF_F_%s_IG_I" % (len(the_forms) + 1)) 
    item.set("Name", form_name) 
    item.set("Datatype", "Text") 
    question = ElementTree.SubElement(item, "{%s}Question" % (odm_namespace))
    translated_text = ElementTree.SubElement(question, "{%s}TranslatedText" % (odm_namespace))
    translated_text.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "en"
    translated_text.text = "Placeholder for activity %s" % (form_name)
    the_items.append(item)
    return form

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))
with driver.session() as session:

    # Choose a protocol from DB
    protocol_name = "DDR"
    brief_title = ""
    official_title = ""

    query = """MATCH (pr:STUDY_PROTOCOL) WHERE pr.brief_title = '%s' 
        RETURN pr.brief_title as brief_title, pr.official_title as official_title, pr.scientific_title as scientific_title""" % (protocol_name)
    result = session.run(query)
    for record in result:
        brief_title = record["brief_title"]
        official_title = record["official_title"]
        scientific_title = record["scientific_title"]
    print("'%s', '%s', '%s'" % (brief_title, official_title, scientific_title))

    # CRF Link
    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESIGN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
        -[]->(v:VISIT)<-[]-(wfi:WORKFLOW_ITEM)-[]->(a:ACTIVITY)-[]->(data:STUDY_DATA) WHERE pr.brief_title = '%s'
        WITH a.description as activity, data.ecrf_link as link
        RETURN DISTINCT activity, link""" % (protocol_name)
    result = session.run(query)
    crf_activities = {}
    for record in result:
        #print("'%s', '%s'" % (record["activity"], record["link"]))
        if not record["activity"] in crf_activities:
            crf_activities[record["activity"]] = []
        crf_activities[record["activity"]].append(record["link"])
    #print(crf_activities)

driver.close()

# Display the CRF
odm = ElementTree.Element("{%s}ODM" % (odm_namespace))
odm.set("FileOID", "DDF_ODM_001") 
odm.set("FileType", "Snapshot") 
odm.set("Granularity", "Metadata") 
odm.set("CreationDateTime", exported_at)
study = ElementTree.SubElement(odm, "{%s}Study" % (odm_namespace))
study.set("OID", "DDF_S_001")
global_variables = ElementTree.SubElement(study, "{%s}GlobalVariables" % (odm_namespace))
study_name = ElementTree.SubElement(global_variables, "{%s}StudyName" % (odm_namespace))
study_name.text = brief_title
study_description = ElementTree.SubElement(global_variables, "{%s}StudyDescription" % (odm_namespace))
study_description.text = scientific_title
protocol_name = ElementTree.SubElement(global_variables, "{%s}ProtocolName" % (odm_namespace))
protocol_name.text = official_title
basic_definitions = ElementTree.SubElement(study, "{%s}BasicDefinitions" % (odm_namespace))
metadata_version = ElementTree.SubElement(study, "{%s}MetaDataVersion" % (odm_namespace))
metadata_version.set("OID", "DDF_MDV_001")
metadata_version.set("Name", "DDF Metadata")
protocol = ElementTree.SubElement(metadata_version, "{%s}Protocol" % (odm_namespace))
study_event_ref = ElementTree.SubElement(protocol, "{%s}StudyEventRef" % (odm_namespace))
study_event_ref.set("StudyEventOID", "DDF_SE_001")
study_event_ref.set("Mandatory", "Yes")
study_event_ref.set("OrderNumber", "1")
study_event_def = ElementTree.SubElement(metadata_version, "{%s}StudyEventDef" % (odm_namespace))
study_event_def.set("OID", "DDF_SE_001")
study_event_def.set("Name", "CRF Book")
study_event_def.set("Repeating", "No")
study_event_def.set("Type", "Scheduled")

the_forms = []
the_item_groups = []
the_items = []
the_code_lists = []

lib = ["001_ODM_TEST.xml", "002_VS.xml", "003_ECG.xml"]

# Go and find the forms. Either use the CRF link or, if not present, use a standard library of forms, see if we have a match
for activity, links in crf_activities.items():
    print(activity)
    for link in links:
        result = None
        if link == "":
            #print("    No CRF link")
            for file in lib:
                xml_doc = ElementTree.parse("lib/%s" % (file))
                #print("    XML Doc", xml_doc)
                result = extract_form(xml_doc, study_event_def, activity, the_forms, the_item_groups, the_items, the_code_lists)
                if result != None:
                    break
        else:
            print("    CRF link detected")
            with urllib.request.urlopen(link) as f:
                xml = f.read() 
                parser = ElementTree.XMLParser(recover=True)
                xml_doc = ElementTree.fromstring(xml, parser)
                print("    XML:", xml_doc)
                result = extract_form(xml_doc, study_event_def, activity, the_forms, the_item_groups, the_items, the_code_lists, False)
        if result == None:
            print("    Blank form needed")
            xml_doc = ElementTree.parse('blank.xml')
            result = blank_form(study_event_def, activity, the_forms, the_item_groups, the_items, the_code_lists)
        else:
            print("    Form added")

# Add the items into the ODM
for form in the_forms:
    metadata_version.append(form)
for item_group in the_item_groups:
    metadata_version.append(item_group)
for item in the_items:
    metadata_version.append(item)
for code_list in the_code_lists:
    metadata_version.append(code_list)

# Write out the XML merged file
the_odm = ElementTree.ElementTree(odm)
the_odm.write("ddf_crf.xml", xml_declaration=True, encoding='utf-8', method="xml")

# Transform the XML into an HTML rendering
xslt = ElementTree.parse("crf.xsl")
transform = ElementTree.XSLT(xslt)
the_crf = transform(odm)
the_crf.write("ddf_crf.html", xml_declaration=True, encoding='utf-8', method="html")