# Transcelerate Digitial Data Flow (DDF) - Simple Examples
## Overview
This Github contains some simple python programs that were used to investigate and prototype the DDF USDM and, in particular, the generation of an SoA and eCRF from the model
## Method
The method chosen was to place a logical representation of the USDM into a Neo4j property graph. This conversion of the USDM UML into a graph representation allowed familiarity with the model to be gained while making prototype implementation easy. The use of Neo4j also allowed the model to be visualized easily.
## Programs
Three programs are available:
-	ddf.py – Loads the DDF data into Neo4j
-	soa.py – Builds the SoA
-	crf.py – Builds an ODM version of the CRF and passes through a stylesheet to render
The programs were put together quickly with the demonstration need in mind rather than efficient coding. A lot of refactoring could take place, especially on the crf.py code and the XML generation
## Neo4j
The code assumes Neo4j is running locally with username and password hardcoded as below; there is no need for a secure setup for this demonstration code. You can change this if needed.
```
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))
```
## CRF Stylesheets
Two CRF stylesheets are used:
- One very old one from 15 years or more back used as part of an FDA demo on ODM. It needs throwing away! :)
- A more modern one by Jørgen Mangor Iversen. This can be found [on Github](https://github.com/jmangori/CDISC-ODM-XML-CRF-SDTM-Annotations).
