import tarfile
from pymongo import MongoClient
import json
import time
import sys
import argparse

parser = argparse.ArgumentParser(description='ORCID Mongo importer')
parser.add_argument('--file', dest="file", help="the .tar.gz JSON datadump file")
parser.add_argument('--collection', dest="collection", help="the mongo collection to import into")
parser.add_argument('--resume', dest="resume", type=int, default=0)
args = parser.parse_args()


print ("ok!!" + args.file)

with open(args.file) as f:
    print(f.read())

client = MongoClient("mongodb://orcid-mongo:27017/testdb")
client.testdb[args.collection].insert_one({"a":args.resume});
