# TransCelerate Digitial Data Flow (DDF) - Simple Examples
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

Note that the crf.py program requires access to the CDISC Library for terminology definitions. The API key is placed into an environment variable as follows

```
API_KEY = os.getenv('CDISC_API_KEY')
```

## Neo4j
The code assumes Neo4j is running locally with username and password hardcoded as below; there is no need for a secure setup for this demonstration code. You can change this if needed.
```
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))
```
## CRF Stylesheets
Two CRF stylesheets are used:
- One very old one from 15 years or more back used as part of an FDA demo on ODM. It needs throwing away! :)
- A more modern one by Jørgen Mangor Iversen of Leo Pharma A/S. This is currently held in a private Github repository.

## Docs Directory
In the documents directory you will find two files, they might be useful
- graph.png - An image of the DDF schema used for this exercise
- dashboard.json - A definitions file for NeoDash. This is a nice tool and allows you to create no code dashboards for Neo4j. You need to install Neo4j desktop but the instructions to do so are straight forward.

## Setup
Usual python setup process, pretty simple, create the virutal environment and install the dependencies.
```
python3 -m venv env
source env/bin/activate
pip install neo4j
pip install beautifultable
```
You might get the warning about upgrading pip, it will tell you what to do
```
...ddf/env/bin/python3 -m pip install --upgrade pip
```