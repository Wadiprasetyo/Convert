import pymongo
import csv

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avengers']
data = list(col.find())
print(data)

with open('data.csv','w', newline='')as x:
    kolom = list(['id','nama','usia'])
    writer = csv.DictWriter(x, fieldnames = kolom)
    writer.writeheader()
    writer.writerows(data)