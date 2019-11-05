# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
# import counter class from collections module 
from collections import Counter 

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '928002030-RadYSeIbxgGaI2zhvizIqWu0s5cRsK3oe4A0DPZd'
ACCESS_SECRET = 'e8pj2Ht7jK3aMmYsXZfACsz67JTxFpYzeeiB1abvYMNnZ'
CONSUMER_KEY = '7a53y0hVHFwUs9Ig0hZ2qKjRP'
CONSUMER_SECRET = '2fw76vVXtclWBxukN45XDhpfqdDjSKrbnuXyi5Nsz1mixsKHNA'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

hashtagsArray = []
tweetsArray = []
urlArray = []
usermentionsArray = []
hashtagsusedArray = []

#Script funcions below

def getTrends(api):
    # Open a file called trends.json and parsing to insert the trending info
    with open('trends.json','w') as f:
        trendsBrasil = api.trends_place(id =23424768)
        json.dump(trendsBrasil,f,indent=4)
    return trendsBrasil

def getHashtags(getTrends,hashtagsArray):
    # Populate the hashtagsArray with the 'name' field of the trend info
    for element in getTrends[0]['trends']:
        hashtagsArray.append(element['name'])
    return hashtagsArray

def getTweets(hashtagsArray):
    # Open a file called tweets.json, parsing, and for each element of the hashtagsArray do the research
    with open('tweets.json','w') as f:
        for element in hashtagsArray:
            tweets = tweepy.Cursor(api.search, q=element, count=10)
    # Doing two copies of the tweets info. One copy for json file and one for variable array inside the script
            for item in tweets.items(10):
                tweetsArray.append((json.dumps(item._json)))
                json.dump(item._json, f, indent=4)
    return tweetsArray

def transformJson():
    # Convert json dictionary in array of dictionaries
    with open('tweets.json', 'r') as f:
        data = f.read()
        newdata = data.replace('}{', '},{')
        jsondata = json.loads(f'[{newdata}]')
        with open('newtweets.json', 'w') as y:
            json.dump(jsondata, y, indent=4)

def parseHashtags():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
    counter = Counter()
    newhashtags = []    
    with open('newtweets.json') as f:
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
    return counter

def parseUrls():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
    counter = Counter()
    newhashtags = []    
    with open('newtweets.json') as f:
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
    return counter

def parseUsersMentions():
    # Count method - ref: https://www.w3schools.com/python/ref_list_count.asp
    counter = Counter()
    newhashtags = []    
    with open('newtweets.json') as f:
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
    return counter


trends = getTrends(api)
hashtagsTrend = getHashtags(trends, hashtagsArray)
tweets = getTweets(hashtagsTrend)
#urls = parseUrls(tweets, urlArray)
#userMentions = parseUsersMentions(tweets, usermentionsArray)
#hashtagsUsed = parseHashtags(tweets, hashtagsusedArray)

#transformJson()
#print (parseHashtags())
#print(parseUrls())
print (parseUsersMentions())