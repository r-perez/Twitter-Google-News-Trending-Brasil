import json
import tweepy
import time
from collections import Counter 

timestr = time.strftime("%Y%m%d-%H")

def parseHashtags():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
    counter = Counter()
    with open('./tweets/transformed/' + timestr + '.json') as f:
        data = json.load(f)
    # For each element of data, being data the json loaded
        for element in data:
    # Runs through hashtags vectors and store the info in an array called hashtags        
            hashtags = (element['entities']['hashtags'])
    # For each element of hashtgs, for each pair item (key and value), if the key is 'text', ident count[value] 
            for each in hashtags:
                for key, value in each.items():
                    if key == 'text':
                        counter[value] += 1
    
    with open('./parsedData/hashtags/'+ timestr + '.json', 'w', encoding='utf-8') as parsed:
        parsed.write(str(counter))

    return counter

def parseUrls():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
    counter = Counter()
    with open('./tweets/transformed/' + timestr + '.json') as f:
        data = json.load(f)
    # For each element of data, being data the json loaded
        for element in data:
    # Runs through hashtags vectors and store the info in an array called hashtags        
            urls = (element['entities']['urls'])
    # For each element of hashtgs, for each pair item (key and value), if the key is 'text', ident count[value] 
            for each in urls:
                for key, value in each.items():
                    if key == 'expanded_url':
                        counter[value] += 1
    
    with open('./parsedData/urls/'+ timestr + '.json', 'w', encoding='utf-8') as parsed:
        parsed.write(str(counter))
    
    return counter

def parseUsersMentions():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
    counter = Counter()
    with open('./tweets/transformed/' + timestr + '.json') as f:
        data = json.load(f)
    # For each element of data, being data the json loaded
        for element in data:
    # Runs through hashtags vectors and store the info in an array called hashtags        
            user_mentions = (element['entities']['user_mentions'])
    # For each element of hashtgs, for each pair item (key and value), if the key is 'text', ident count[value] 
            for each in user_mentions:
                for key, value in each.items():
                    if key == 'screen_name':
                        counter[value] += 1
    
    with open('./parsedData/mentions/'+ timestr + '.json', 'w', encoding='utf-8') as parsed:
        parsed.write(str(counter))
    
    return counter

parseHashtags()
parseUrls()
parseUsersMentions()