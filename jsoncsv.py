import json
import csv

with open('x.json') as x:
        data = json.load(x)
print(data)

with open('x.csv', 'w',newline='') as x:
    kolom = ['nama', 'usia', 'kota']
    tulis = csv.DictWriter(x, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(data)