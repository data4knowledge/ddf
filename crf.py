# Code for generating an SoA from a DDF graph database
# Code has been quickly put together to get the desired outputs rather than
# making the code as elegant. It mitem_groupht be possible to merge the queries or 
# have them return more easily consumed results

from neo4j import GraphDatabase
from beautifultable import BeautifulTable

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))

#with driver.session() as session:

    # Choose a protocol from DB
#    protocol_name = "DDR"

    # CRF Link
#    query = """MATCH (pr:STUDY_PROTOCOL)<-[]-(s:STUDY)-[]->(sd:STUDY_DESitem_groupN)-[]->(sc:STUDY_CELL)-[]->(e:STUDY_EPOCH)
#        -[]->(v:VISIT)<-[]-(wfi:WORKFLOW_ITEM)-[]->(a:ACTIVITY)-[]->(data:STUDY_DATA) WHERE pr.brief_title = '%s'
#        WITH wfi.description as activity, data.ecrf_link as link
#        RETURN DISTINCT activity, link""" % (protocol_name)
#    result = session.run(query)
#    crf_activities = {}
#    for record in result:
#        print("'%s', '%s'" % (record["activity"], record["link"]))
#        if not record["activity"] in crf_activities:
#            crf_activities[record["activity"]] = []
#        crf_activities[record["activity"]].append(record["link"])
#    print(crf_activities)

#driver.close()

# Display the CRF
#import urllib.request

#for activity, links in crf_activities.items():
#    for link in links:
#        if link != "":
#            with urllib.request.urlopen(link) as f:
#                xml = f.read().decode('utf-8')
#                print(link)
#                #print(xml)

import lxml.etree as ElementTree


#from xml.etree import ElementTree
import datetime

exported_at = datetime.datetime.now().replace(microsecond=0).isoformat()

odm = ElementTree.Element("ODM")
odm.set("FileOID", "DDF_ODM_001") 
odm.set("FileType", "Snapshot") 
odm.set("Granularity", "Metadata") 
odm.set("CreationDateTime", exported_at)
study = ElementTree.SubElement(odm, "Study")
study.set("OID", "DDF_S_001")
global_variables = ElementTree.SubElement(study, "GlobalVariables")
study_name = ElementTree.SubElement(global_variables, "StudyName")
study_name.text = "Study Name Here"
study_description = ElementTree.SubElement(global_variables, "StudyDescription")
study_description.text = "Study Description Here"
protocol_name = ElementTree.SubElement(global_variables, "ProtocolName")
protocol_name.text = "Protocol Name Here"
basic_definitions = ElementTree.SubElement(study, "BasicDefinitions")
metadata_version = ElementTree.SubElement(study, "MetaDataVersion")
metadata_version.set("OID", "DDF_MDV_001")
metadata_version.set("Name", "DDF Metadata")
protocol = ElementTree.SubElement(metadata_version, "Protocol")
study_event_ref = ElementTree.SubElement(protocol, "StudyEventRef")
study_event_ref.set("StudyEventOID", "DDF_SE_001")
study_event_ref.set("Mandatory", "Yes")
study_event_ref.set("OrderNumber", "1")
study_event_def = ElementTree.SubElement(metadata_version, "StudyEventDef")
study_event_def.set("OID", "DDF_SE_001")
study_event_def.set("Name", "CRF Book")
study_event_def.set("Repeating", "No")
study_event_def.set("Type", "Scheduled")
#				<FormRef FormOID="0001_F_BASELINE" Mandatory="Yes" OrderNumber="1"/>

the_forms = []
the_item_groups = []
the_items = []
the_code_lists = []

mytree = ElementTree.parse('odm.xml')
myroot = mytree.getroot()
forms = mytree.findall('//{http://www.cdisc.org/ns/odm/v1.3}FormDef[@Name="Baseline Visit Form"]')
form = forms[0]
the_forms.append(form)
form_ref = ElementTree.SubElement(study_event_def, "FormRef")
form_ref.set("FormOID", form.attrib["OID"])
form_ref.set("Mandatory", "Yes")
form_ref.set("OrderNumber", "1")

item_group_refs = form.findall('{http://www.cdisc.org/ns/odm/v1.3}ItemGroupRef')
for item_groupref in item_group_refs:
    oid = item_groupref.attrib['ItemGroupOID']
    item_groups = mytree.findall("//{http://www.cdisc.org/ns/odm/v1.3}ItemGroupDef[@OID='%s']" % (oid)) 
    item_group = item_groups[0]
    the_item_groups.append(item_group)
    item_refs = item_group.findall('{http://www.cdisc.org/ns/odm/v1.3}ItemRef')
    for item_ref in item_refs:
        oid = item_ref.attrib['ItemOID']
        items = mytree.findall("//{http://www.cdisc.org/ns/odm/v1.3}ItemDef[@OID='%s']" % (oid)) 
        item = items[0]
        the_items.append(item)
        code_list_refs = item.findall('{http://www.cdisc.org/ns/odm/v1.3}CodeListRef')
        for code_list_ref in code_list_refs:
            oid = code_list_ref.attrib['CodeListOID']
            code_lists = mytree.findall("//{http://www.cdisc.org/ns/odm/v1.3}CodeList[@OID='%s']" % (oid)) 
            code_list = code_lists[0]
            the_code_lists.append(code_list)
        measurement_unit_refs = item.findall('{http://www.cdisc.org/ns/odm/v1.3}MeasurementUnitRef')
        for measurement_unit_ref in measurement_unit_refs:
            oid = measurement_unit_ref.attrib['MeasurementUnitOID']
            measurement_units = mytree.findall("//{http://www.cdisc.org/ns/odm/v1.3}MeasurementUnit[@OID='%s']" % (oid)) 
            if measurement_units:
                measurement_unit = measurement_units[0]
                basic_definitions.append(measurement_unit)

for form in the_forms:
    metadata_version.append(form)
for item_group in the_item_groups:
    metadata_version.append(item_group)
for item in the_items:
    metadata_version.append(item)
for code_list in the_code_lists:
    metadata_version.append(code_list)

tree = ElementTree.ElementTree(odm)
tree.write("ddf_crf.xml", xml_declaration=True, encoding='utf-8', method="xml")

xslt = ElementTree.parse("crf.xsl")
transform = ElementTree.XSLT(xslt)
newdom = transform(odm)
#print(ElementTree.tostring(newdom, pretty_print=True))

