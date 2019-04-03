import requests
from urllib.parse import urlparse

def get1000Result(keyword) :
    list = []
    for num in range (0, 10) :
        list = list + call(keyword, num * 100 + 1)['items']
    return list

def call(keyword,start):
    r_id = open('naver_api_id.txt')
    r_secret = open('naver_api_secret.txt')

    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100&start="+str(start)
    header = {"X-Naver-Client-Id":r_id.read(),"X-Naver-Client-Secret":r_secret.read()}
    result = requests.get(urlparse(url).geturl(),headers=header)
    print(result.status_code)
    return result.json()
