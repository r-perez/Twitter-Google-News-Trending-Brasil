import json
import tweepy
import time
from collections import Counter 

#timestr = time.strftime("%Y%m%d-%H")
timestr = '20200208-10'
array = []
newarray = []

def parse():
      with open('./parsedData/mentions/20200509-20' + '.json', 'r', encoding='utf-8') as parsed:
        for item in parsed:
          if item != "Counter({\n" and item != '})' and item != ",":
#looping for clean '\n' at the end of items
            array.append(parsed.readline()[:-1])
#looping for clean ',' at the end of items
        for item in array:
          newarray.append()
          sub_dict = {}
          print(newarray)
          sub_dict['user'] = item[0]
          #(item[:-1])
          #print(item)
        #print(newarray)
        json_newarray = json.dumps(newarray)
        #print(json_newarray)
      
parse()
