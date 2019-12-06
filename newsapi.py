from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='2de5d157d448424db4574be570b492d4')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='SegundaChamada',
                                          language='pt',
                                          country='br')
print(top_headlines)