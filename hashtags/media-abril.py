import os, json
import pandas as pd
from os import listdir
from os.path import isfile, join

import itertools
from collections import Counter

#open json files in the path
json_files = [pos_json for pos_json in os.listdir('./') if pos_json.endswith('.json')]
#create a list with lists of files based on the files name
groups =  [list(g) for _, g in itertools.groupby(sorted(json_files), lambda x: x[0:8])]

hashtags = []
dates = []
hashtags_list = []

df = pd.DataFrame(columns=['hashtags','dates'])

for group in groups:
    #for each file in the group
    for file in group:
        #if the file is not empty
        if os.stat('./' + file).st_size != 0:
            #open file for read
            with open('./' + file, "r") as infile:
                #load json file content and append
                json_file = json.load(infile)                
                ci1 = [i['name'] for i in json_file[0]['trends']]
                hashtags.append(ci1)

                                #get prefix 8 characters of files names
                for hashtag in ci1:
                    name = os.path.basename(infile.name)
                    name = name[0:8]
                    dates.append(name)

for each in hashtags:
    for hashtag in each:
        hashtags_list.append(hashtag)

        
df = pd.DataFrame({'Hashtags':hashtags_list, 'Dates':dates})
#df['dates'] = dates


df.to_csv(r'./media-hashtags.csv', index=False, header=True)