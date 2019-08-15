import csv
import mysql.connector

lists=[]
with open('data.csv','r') as x:
    reader = csv.DictReader(x)
    for x in reader:
        lists.append(dict(x))
print(lists)

dbku = mysql.connector.connect(
    host = '<host>',
    port = 3306,
    user = '<user>',
    passwd = '<password>',
    database = 'chevalier'
)
kursor = dbku.cursor()
keys = []
for loop in range(len(lists)):
    for key in lists[loop].keys():
        keys.append(key)
key1 = sorted(list(set(keys)))
print(key1)

kursor.execute('create table karakter1( {} varchar(50))'.format(key1[0]))
for item in range(len(key1)-1):
    kursor.execute('alter table karakter1 add column {} varchar(50)'.format(key1[item+1]))
    dbku.commit()

keys = []
vals = []
for key in lists:
    keys.append(tuple(key.keys()))
for val in lists:
    vals.append(tuple(val.values()))
print(vals)

for key,val in zip(keys,vals):
    querydb = f'''insert into karakter1 {str(key).replace("'",'')} values{str(val).replace(')','')})'''
    print(querydb)
    kursor.execute(querydb)
    dbku.commit()