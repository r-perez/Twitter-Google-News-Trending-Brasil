import os, json
import pandas as pd

path_to_json = './google-news/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

jsons_data = pd.DataFrame(columns=['name','url'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        name = json_text['articles'][0]['source']['name']
        url = json_text['articles'][0]['url']

        jsons_data.loc[index] = [name, url]

        jsons_data.sort_values('name')

print(jsons_data)