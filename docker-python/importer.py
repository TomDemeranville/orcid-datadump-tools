#python -m pip install pymongo
import tarfile
from pymongo import MongoClient
import json
import time
import sys

parser = argparse.ArgumentParser(description='ORCID Mongo importer')
parser.add_argument('--file', dest="file", help="the .tar.gz JSON datadump file")
parser.add_argument('--collection', dest="collection", help="the mongo collection to import into")
parser.add_argument('--resume', dest="resume", type=int, default=0)
args = parser.parse_args()

#create collection from param
client = MongoClient()
db = client.orcid
collection = db[args.collection]

batch = []
count = 0;
start_time=time.time()

resume = 0
skip_count = 0
count = 0
#resume?
if args.resume:
	resume = int(args.resume)
	count += resume

#pass tar file in as param
tar = tarfile.open(args.file, 'r|gz') 

#batch up the json and insert into mongo
for tar_info in tar:
	if tar_info.isfile():
		skip_count += 1
		if skip_count > resume:
			if (tar_info.size < 16777216):
				f = tar.extractfile(tar_info)
				batch.append(json.loads(f.read()))
			else:
				print ("{} too large {} bytes".format(tar_info.name,tar_info.size))
		if len(batch) > 9999:
			count += len(batch)
			collection.insert_many(batch)
			tar.members = []
			batch = []
			elapsed_time=time.time()-start_time
			print ("elapsed: {}s - count: {:0.2f}".format(elapsed_time, count))

if len(batch) > 0:
	collection.insert_many(batch)
	elapsed_time=time.time()-start_time
	print ("elapsed: {}s - count: {:0.2f}".format(elapsed_time, count,2))

print ("removing locked and depreciated records")
collection.delete_many({"response\u002Dcode":{"$exists": True}})
print ("creating orcid.identifier.path index")
collection.create_index([('orcid\u002Didentifier.path', 1)],unique=True)

	
