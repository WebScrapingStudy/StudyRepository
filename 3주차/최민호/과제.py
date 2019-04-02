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
client_id = r.read(20)
client_secret = r.read(10)

print(client_id)
print(client_secret)
print(len(client_id))
print(len(client_secret))
encText = urllib.parse.quote("부경대 카페")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/search/blog.xml?query=" +search
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
