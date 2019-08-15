import json
import csv

data = []
with open('data.csv', 'r') as x:
    reader = csv.DictReader(x)
    for i in reader:
        data.append(dict(i))

with open('x.json','w') as x:
        json.dump(data, x)