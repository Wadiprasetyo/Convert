import mysql.connector
import pymongo

dbku = mysql.connector.connect(
    host = '<host>',
    port = 3306,
    user = 'user',
    passwd = 'password',
    database = 'chevalier'
)

kursor = dbku.cursor()
querydb = '''select * from karakter'''
kursor.execute(querydb)

list1 = kursor.fetchall()
dicts = [{'id': item [0],'nama':item[1],'usia':item[2]}for item in list1]

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avenger']

for item in dicts:
    y = col.insert_one(item)