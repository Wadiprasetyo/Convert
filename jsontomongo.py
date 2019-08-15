import pymongo
import json
x= pymongo.MongoClient('mongodb://localhost:27017')

db=x['marvel']
col=db['avengers']

with open('data.json') as x:
    data=json.load(x)

for i in data:
    col.insert_one(i)