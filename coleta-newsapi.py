from newsapi import NewsApiClient
import time
from datetime import datetime,timedelta

startTime = time.time()
now = datetime.now()
strtoday = now.strftime("%Y-%m-%d")
stryesterday = datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')
# Init
newsapi = NewsApiClient(api_key='2de5d157d448424db4574be570b492d4')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='pt',
                                          country='br',
                                          from_param='stryesterday',
                                          to='strtoday')