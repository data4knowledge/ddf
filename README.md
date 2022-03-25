# TransCelerate Digitial Data Flow (DDF) and Unified Study Definition Model (USDM) - Prototype and Demonstration Code

## Overview
This Github contains some simple python programs that were used to investigate and prototype the DDF USDM and, in particular, the generation of an SoA and eCRF from the model.

The project is a collaboration between Transcelerate and CDISC and more information can be found [here on the TransCelerate site](https://www.transceleratebiopharmainc.com/initiatives/digital-data-flow/) and on the [CDISC web site](https://www.cdisc.org/ddf)

## Disclaimer
Nothing in this repository should be taken as definitive or normative and does not speak for either Transcelerate or CDISC. The code here is for prototyping and demonstration purposes only and is provided as is.

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

The program also uses a local library of ODM files as well as a remote set (currently held on a dropbox installation). Some of these were taken from [the CDISC eCRF portal](https://www.cdisc.org/kb/ecrf).

## Neo4j
The code assumes Neo4j is running locally (default setup) with username and password hardcoded as below; there is no need for a secure setup for this demonstration code. You can change this if needed.
```
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "ddf"))
```

It is recommended to install the Neo4j using the desktop offering. This gives you access to the normal browser tool but also over tools such as NeoDash. NeoDash is a nice tool and allows you to create no code dashboards for Neo4j. See [the Neo4j download page](https://neo4j.com/download/). 

## CRF Stylesheets
Two CRF stylesheets are used:
- One very old one from 15 years or more back used as part of an FDA demo on ODM. It needs throwing away! :)
- A more modern one courtesy of Jørgen Mangor Iversen of Leo Pharma A/S. This is currently held in a private Github repository but a copy is included within this repository but is, of course, just a snapshot of the one used.

## Docs Directory
In the documents directory you will find two files, they might be useful
- graph.png - An image of the DDF schema used for this exercise
- dashboard.json - A definitions file for NeoDash. 

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