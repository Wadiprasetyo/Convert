import mysql.connector
import json

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'user',
    passwd = 'pass',
    database = 'chevalier'
)

kursor = dbku.cursor()
querydb = '''select * from karakter'''
kursor.execute(querydb)

list1 = kursor.fetchall()
dict1 = [{"id":i[0],"nama":i[1],"usia":i[2]} for i in list1]

with open("sqlcjson.json","w") as x :
    x.write(str(dict1).replace("'",'"'))