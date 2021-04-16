import re
# import codecs
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

link = []
twitter = []
youtube = []
insta = []
website = []
facebook = []
name = []
job = []
udemy = requests.get("https://www.udemy.com/user/robpercival/")
# dawaii = requests.get("https://www.servaid.com.pk/products/fetch/medicine/conventional-agents?page=2")
# html = dawaii.content
# info = bs(codecs.open('dawaii.html', 'r'), features='html.parser')

info = bs(udemy, features='html.parser')

# results = info.find_all(string=re.compile('.*{0}.*'.format('@')), recursive=True)
# print(results)

# print(info.prettify())
title = info.find('title')
nam = str(title.text).split('|')
name.append(nam[0].strip('\n').strip())
job.append(nam[1].strip('\n').strip())
k1 = (info.find_all('div', attrs={'class': 'instructor-profile--social-links--3Kub5'}))
k2 = str([m.find_all('a') for m in k1]).split('a class')
for k in k2:
    if 'href' in k:
        if 'personal-website-link' in k:
            website.append((k[k.index('href') + 6:k.index('>')]).replace('"', ''))
        if 'twitter-link' in k:
            twitter.append((k[k.index('href') + 6:k.index('>')]).replace('"', ''))
        if 'facebook-link' in k:
            facebook.append((k[k.index('href') + 6:k.index('>')]).replace('"', ''))
        if 'youtube-link' in k:
            youtube.append((k[k.index('href') + 6:k.index('>')]).replace('"', ''))

data = [name, job, website, twitter, facebook, youtube]
df = pd.DataFrame(data, index=['name', 'job', 'website', 'twitter', 'facebook', 'youtube'])
tdf = df.T
# tdf.to_csv('Udemy.csv', encoding='utf-8-sig', index=False)
