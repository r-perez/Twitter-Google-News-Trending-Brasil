import json
import tweepy
import time
from collections import Counter 

#timestr = time.strftime("%Y%m%d-%H")
timestr = '20200208-10'

def parse():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
      with open('./parsedData/mentions/20200510-02' + '.json', 'r', encoding='utf-8') as parsed:
        for item in parsed:
          print(item)
"""             text = json.loads(item)
            text.replace("'",'"')
            print(text) """

parse()
