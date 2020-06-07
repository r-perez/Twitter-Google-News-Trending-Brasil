import os, json
import pandas as pd
from os import listdir
from os.path import isfile, join
import itertools

path_to_json = './hashtags/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

groups =  [list(g) for _, g in itertools.groupby(sorted(json_files), lambda x: x[0:8])]

result = []

#groups is a vector of vectors
for group in groups:
    #file is string index of a group vector
    for file in group:
        print(file)
        with open(path_to_json + file, "r") as infile:
            result.append(json.load(infile))
            #print(result)
            files_name = os.path.basename(infile.name)[0:8]
            with open(path_to_json + 'merged/' + files_name + ".json", "w") as outfile:
                json.dump(result, outfile)
            result = []
    

""" hashtags_data = pd.DataFrame(columns=['hashtag','url'])

onlyfiles = [f for f in listdir(path_to_json) if isfile(join(path_to_json, f))]

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        
        json_text = json.load(json_file)

        hashtag = json_text[0]['trends'][0]['name']
        print(hashtag)
 """
        #url = json_text[0]['trends'][0]['url']
        
        #for file in onlyfiles:
        #    date = file
        
        #hashtags_data.loc[index] = [hashtag, url]

#print(hashtags_data)