import os
import requests
from urllib.parse import quote
from os import chdir
import json

#get current path
path = os.getcwd();
print(path)
#change path
os.chdir('c:\\Users\\Minho\\Desktop\\WebScrapping\\StudyRepository\\3주차\\최민호')
#os.chdir(r"c:\Users\Minho\Desktop\WebScrapping\StudyRepository\3주차\최민호")
print(os.getcwd())

def get1000Result(keyword):
    list = []
    for num in range(0,10):
        list = list + call("부경대 카페",num*100+1)['items']
    return list

def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query="


result = get1000Result("부경대 카페")
file = open("./pknutaste.json", "w+")
file.write(json.dumps(list))