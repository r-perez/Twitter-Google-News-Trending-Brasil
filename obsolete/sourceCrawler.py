import os, json
import pandas as pd
import itertools


path_to_json = './google-news/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

groups =  [list(g) for _, g in itertools.groupby(sorted(json_files), lambda x: x[0:8])]

df = pd.DataFrame(columns=['name','url'])

groups_size = len(groups[0])
#print(groups_size)
each_file = []
#for each group of files of the same day
for group in groups:
    #for each file in the group
    for i in range(0, groups_size, 1):
        #if os.stat(path_to_json + file).st_size != 0:
        print(groups[i])
        each_file.append(groups[i])


    

"""         with open(os.path(path_to_json,each_file)) as json_content:
            print(json_content) """
            
"""         name = json_text['articles'][0]['source']['name']
        url = json_text['articles'][0]['url']

        df.loc[index] = [name, url]

        df.sort_values('name')

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        name = json_text['articles'][0]['source']['name']
        url = json_text['articles'][0]['url']

        df.loc[index] = [name, url]

        df.sort_values('name')

print(df) """