import pandas as pd
import json
import numpy 

with open('./perguntacorona/perguntacorona-expanded.json', encoding='utf-8') as f:
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
    text = []
    tweet_url = []
    user_id = []
    username = []
    
    i=0
    for entity in inputdata:

        hashtags.append(inputdata[i]['hashtags'])
        date.append(inputdata[i]['timestamp'])
        img_urls.append(inputdata[i]['img_urls'])
        video_url.append(inputdata[i]['video_url'])
        replies.append(inputdata[i]['replies'])
        reply_to_users.append(inputdata[i]['reply_to_users'])
        retweets.append(inputdata[i]['retweets'])
        links.append(inputdata[i]['links'])        
        text.append(inputdata[i]['text'])
        text_content = text[i]
        tweet_id.append(inputdata[i]['tweet_id'])
        tweet_url.append(inputdata[i]['tweet_url'])
        user_id.append(inputdata[i]['user_id'])
        username.append(inputdata[i]['username'])

        user_mentions.append([x for x in text_content.split() if (x.startswith('@') or (x.startswith('.@')))])

        i += 1
    
    for each in user_mentions:
        for mention in each:
            if mention.startswith('.'):
                mention.replace('.', '')


d = {'tweet_id':tweet_id, 'user_id':user_id, 'username':username, 'text':text, 'hashtags':hashtags, 'date':date, 'img_urls':img_urls, 'video_url':video_url, 'replies':replies, 'reply_to_users':reply_to_users, 'retweets':retweets, 'links':links, 'user_mentions':user_mentions}
df = pd.DataFrame(d)
#df = df.explode('hashtags')
#df = df.explode('user_mentions')
df.to_csv('perguntacorona-expanded-text.csv', index=False)
#df = pd.DataFrame(data = d, columns=['hashtags','date', 'img_urls', 'video_url', 'replies', 'reply_to_users', 'retweets'])

#print(df)
