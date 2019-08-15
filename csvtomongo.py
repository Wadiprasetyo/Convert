import csv
import pymongo

lists=[]
with open('data.csv','r') as x:
    reader = csv.DictReader(x)
    for x in reader:
        lists.append(dict(x))
# print(lists)

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avenger']
for i in lists:
    col.insert_one(i)