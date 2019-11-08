import json
import tweepy
import time

timestr = time.strftime("%Y%m%d-%H")


def transformJson():
    # Convert json dictionary in array of dictionaries
    with open('./tweets/' + timestr + '.json', 'r') as f:
        data = f.read()
        newdata = data.replace('}{', '},{')
        jsondata = json.loads(f'[{newdata}]')
        with open('./tweets/transformed/' + timestr + '.json', 'w') as y:
            json.dump(jsondata, y, indent=4)


transformJson()