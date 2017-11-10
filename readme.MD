ORCID datadump to Mongo
=======================

This python3 script takes the ORCID JSON datadump and loads it directly into MongoDB.
This is orders of magnitude quicker than extracting it to the file system.

dependencies
------------
you need pymongo

	python3 -m pip install pymongo
and a mongo instance.  Either install locally, or use docker:

	docker run --name orcid-mongo -v /Volumes/Transcend/docker/mongostorage/:/data/db -d mongo:3.5

Usage
-----
have an instance of mongo running

	python3 importer.py --file filename.tar.gz --collection target-collection-name

other scripts
-------------
dump_to_scholix_v2api.js : this takes the dump (in mongo) and transforms it into a scholix like format

Docker
------
This also works with docker

To start mongo:

	docker run --name orcid-mongo -d -p 27017:27017 -v /Volumes/Transcend/docker/mongostorage/:/data/db mongo:3.5

To start the scipt

	cd docker-python
	docker build -t orcid-mongo-import .
	docker run --name importer --link orcid-mongo:orcid-mongo --rm orcid-mongo-import --file myFile.tar.gz --collection myCollection --resume 0 

To run the script again

	docket start importer
