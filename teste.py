import json
import tweepy
import time
from collections import Counter 

#timestr = time.strftime("%Y%m%d-%H")
timestr = '20200208-10'
array = []
newarray = []
sub_dict = {}

def parse():
      with open('./parsedData/mentions/20200509-20' + '.json', 'r', encoding='utf-8') as parsed:
        for item in parsed:
          if item != "Counter({\n" and item != '})' and item != ",":
#looping for clean '\n' at the end of items
            array.append(parsed.readline()[:-1])
#looping for clean ',' at the end of items
        for item in array:
          parts = item.split(":")
          print(parts)
          for part in parts:
            print(part[2])
"""           item_key = parts[0]
          item_val = parts[1]
          print[item_key] """
"""           for part in parts:
            sub_dict.update({part[0],part[1]})
          #newarray.append()
          print(sub_dict) """
          #(item[:-1])
          #print(item)
        #print(newarray)
        #json_newarray = json.dumps(newarray)
        #print(json_newarray)
      
parse()
