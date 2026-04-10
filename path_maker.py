from glob import glob
import os
import json

path = 'paths'
files = glob('*.json')

if os.path.isfile(path):
    with open(path, 'r') as f:
        data = json.load(f)
else:
    data = []

for file in files:
    n = file.replace('.json', '')
    if n not in data:
        data.append(n)

with open(path,'w') as f1:
    json.dump(data, f1, indent=4)
