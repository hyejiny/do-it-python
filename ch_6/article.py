import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(),'html.parser')

# 기사 제목 추출하기
for i in soup.find_all('a',{"class":"link_txt"}):
    # print(i.text)
    # 하이퍼링크 추출
    print(i.get('href'))