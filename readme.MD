ORCID datadump to Mongo
=======================

This python3 script takes the ORCID JSON datadump and loads it directly into MongoDB
This is orders of magnitude quicker than extracting it to the file system.

dependencies
============
python3 -m pip install pymongo

Usage
=====
python3 importer.py <filename.tar.gz> <target-collection-name>

