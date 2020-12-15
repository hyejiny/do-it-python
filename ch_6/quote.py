import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


url = 'https://quotes.toscrape.com/'
# 해당 웹 사이트에 원하는 정보를 요청해서 그 결과물을 반환
html = ur.urlopen(url)
# print(html.read()[:100])

# 뷰리풀숩 활용해서 html에 저장한 자료를 정보를 쉽게 추출할 수 있도록(파싱하기 쉬운 형태)로 변환
soup = bs(html.read(), 'html.parser')
# print(soup)

# 특정 태그 추출
for i in soup.find_all('div',{"class":"quote"}):
    print(i.text)