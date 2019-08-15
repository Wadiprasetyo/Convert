import json
import mysql.connector

#read json
with open('x.json') as x:
    data = json.load(x)
print(data)


dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = '<user>',
    passwd = '<password>',
    database = 'chevalier'
)
kursor = dbku.cursor()
keys = []
for loop in range(len(data)):
    for key in data[loop].keys():
        keys.append(key)
key1 = sorted(list(set(keys)))
print(key1)

kursor.execute('create table karakter( {} varchar(50))'.format(key1[0]))
for item in range(len(key1)-1):
    kursor.execute('alter table karakter add column {} varchar(50)'.format(key1[item+1]))
    dbku.commit()

keys = []
vals = []
for key in data:
    keys.append(tuple(key.keys()))
for val in data:
    vals.append(tuple(val.values()))
print(vals)

for key,val in zip(keys,vals):
    querydb = f'''insert into karakter {str(key).replace("'",'')} values{str(val).replace(')','')})'''
    print(querydb)
    kursor.execute(querydb)
    dbku.commit()