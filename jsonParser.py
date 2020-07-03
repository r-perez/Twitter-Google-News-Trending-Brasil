import pandas as pd
import json
import numpy 

with open('./perguntacorona-expanded.json', encoding='utf-8') as f:
    inputdata = json.load(f)
    hashtags = []
    date = []
    img_urls = []
    video_url = []
    replies = []
    reply_to_users = []
    retweets = []
    tweet_id = []
    links = []
    user_mentions = []
    
    i=0
    for entity in inputdata:

        hashtags.append(inputdata[i]['hashtags'])
        date.append(inputdata[i]['timestamp'])
        img_urls.append(inputdata[i]['img_urls'])
        video_url.append(inputdata[i]['video_url'])
        replies.append(inputdata[i]['replies'])
        reply_to_users.append(inputdata[i]['reply_to_users'])
        retweets.append(inputdata[i]['retweets'])
        tweet_id.append(inputdata[i]['tweet_id'])
        links.append(inputdata[i]['links'])        

        text = inputdata[i]['text']
        user_mentions.append([x for x in text.split() if (x.startswith('@') or (x.startswith('.@')))])

        i += 1
    
    for each in user_mentions:
        for mention in each:
            if mention.startswith('.'):
                mention.replace('.', '')


d = {'tweet_id':tweet_id, 'hashtags':hashtags, 'date':date, 'img_urls':img_urls, 'video_url':video_url, 'replies':replies, 'reply_to_users':reply_to_users, 'retweets':retweets, 'links':links, 'user_mentions':user_mentions}
df = pd.DataFrame(d)
#df = df.explode('hashtags')
df = df.explode('user_mentions')
df.to_csv('perguntacorona-expanded-mentions.csv', index=False)
#df = pd.DataFrame(data = d, columns=['hashtags','date', 'img_urls', 'video_url', 'replies', 'reply_to_users', 'retweets'])

#print(df)
