import time

timestr = time.strftime("%Y%m%d-%H%M%S")

with open('./testes/'+ timestr + '.txt', 'w', encoding='utf-8') as parsed:
    parsed.write(timestr)