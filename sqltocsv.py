import mysql.connector
import csv

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
with open('sqlccsv.csv','w', newline = '') as x :
    writer = csv.DictWriter(x, fieldnames=["id","nama","usia"])
    writer.writeheader()
    writer.writerows(dict1)