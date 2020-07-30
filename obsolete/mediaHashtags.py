import os, json
import pandas as pd
from os import listdir
from os.path import isfile, join
import itertools
from collections import Counter

path_to_json = './hashtags/'
#open json files in the path
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
#create a list with lists of files based on the files name
groups =  [list(g) for _, g in itertools.groupby(sorted(json_files), lambda x: x[0:8])]

files_name = []
urls = []
dates = []
hashtags = []
hashtags_list = []
urls_list = []


df = pd.DataFrame(columns=['hashtags','urls','dates'])

#for each group of files of the same day
for group in groups:
    #for each file in the group
    for file in group:
        #if the file is not empty
        if os.stat(path_to_json + file).st_size != 0:
            #open file for read
            with open(path_to_json + file, "r") as infile:
                #load json file content and append             
                json_file = json.load(infile)                
                ci1 = [i['name'] for i in json_file[0]['trends']]
                hashtags.append(ci1)
                ci2 = [i['url'] for i in json_file[0]['trends']]           
                urls.append(ci2)

                #get prefix 8 characters of files names
                for hashtag in ci1:
                    name = os.path.basename(infile.name)
                    name = name[0:8]
                    dates.append(name)

for eachone in hashtags:
    for hashtag in eachone:
        hashtags_list.append(hashtag)
for eachone in urls:
    for url in eachone:
        urls_list.append(url)

        
df = pd.DataFrame({'Hashtags':hashtags_list,'Urls':urls_list, 'Dates':dates})
#df['dates'] = dates


df.to_csv(r'./media-hashtags.csv', index=False, header=True)