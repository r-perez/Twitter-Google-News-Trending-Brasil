import json
import csv
import re
import sys

import itertools
from collections import Counter

#open json files in the path
json_files = [pos_json for pos_json in os.listdir('./') if pos_json.endswith('.json')]
#create a list with lists of files based on the files name
groups =  [list(g) for _, g in itertools.groupby(sorted(json_files), lambda x: x[0:8])]

print(groups)

with open(file, encoding='utf-8') as f:
    json_content = json.load(f)
    print(json_content[0][0]['trends'])