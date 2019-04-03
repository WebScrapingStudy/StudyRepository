import os
import sys
import urllib.request
import requests
from urllib.parse import urlparse
from urllib.parse import quote
from os import chdir

#change path
os.chdir('c:\\Users\\Minho\\Desktop\\WebScrapping\\StudyRepository\\3주차\\최민호')

r = open('./token.txt', mode='rt', encoding='utf-8')
keyword = "대연동 카페"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
header = {"X-Naver-Client-Id":r.read(20), "X-Naver-Client-Secret":r.read(10)}
result = requests.get(urlparse(url).geturl(),headers = header)
json_obj = result.json()
print(json_obj)