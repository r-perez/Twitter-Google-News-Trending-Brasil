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

def getHashtags(trendsBrasil,hashtagsArray):
    # Populate the hashtagsArray with the 'name' field of the trend info
    for element in trendsBrasil[0]['trends']:
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

def parseUrls(tweets,urlArray):
    cnt = Counter()

    for element in tweets['entities']:
        urlArray.append(element['urls'])
    for word in urlArray:
        cnt[word] += 1
    return urlArray, cnt

def parseUsersMentions(tweets,usermentionsArray):
#Trying to count elements from the arrays
    cnt = Counter()
    for element in tweets['entities']:
        usermentionsArray.append(element['user_mentions']['screen_name'])
    for each in usermentionsArray:
        cnt[each] += 1
    return usermentionsArray, cnt #need to return only the cnt


def parseHashtags(tweets,hashtagsusedArray):

    for element in tweets['entities']:
        hashtagsusedArray.append(element['hashtags']['text'])
    return hashtagsusedArray

trends = getTrends(api)
hashtagsTrend = getHashtags(trends, hashtagsArray)
tweets = getTweets(hashtagsTrend)
urls = parseUrls(tweets, urlArray)
userMentions = parseUsersMentions(tweets, usermentionsArray)
hashtagsUsed = parseHashtags(tweets, hashtagsusedArray)

parseUrls(tweets)