"""
{"name":"minho", "age": 26}           #key , value로 이루어짐 / ""는 문자열
[{"name":"minho", "age": 26}]         #[]안에 item은 1개 들어있음.
[{"name":"minho", "age": 26}]         #{}안에 item은 2개 들어있음. 

#표 형태의 데이터를 json으로 표현하기
[
    {"name":"minho","age":26, "math":90},
    {"name":"bomi","age":25,"math":85}
]
"""
#tag 태그 <ul></ul> <a />
#property 속성 class, id, href, title, src
#property value 속성값 class="greet"에서 greet이 속성값
#<a href="www.google.com">구글</a> 
# => 태그는 <a>  속성은 href 속성값은 www.google.com

"""18강 네이버 API Token발급받기 """
# App Name : Test


import os
import sys
import urllib.request
<<<<<<< HEAD
client_id = "UT1da6xBXa7fCjltgysw"
client_secret = "lgopUhVpqo"
=======
client_id = ""
client_secret = ""
>>>>>>> 628be50e9cb03a4166d7a016d333a42bf0c487c1
encText = urllib.parse.quote("IBK기업은행")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

"""
import requests
from urllib.parse import urlparse

keyword = "방향제"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(), 
headers ={"X-Naver-Client-Id" :"",
          "X-Naver-Client-Secret":""})

json_obj = result.json()
print(json_obj)
"""
#from pathlib import Path
#import os

#p = Path(__file__).parents[1] + '/최민호/hello.csv'
#print(p)

#path = 'C:/Users/Minho/Desktop/WebScrapping/StudyRepository/3주/최민호'
#file = open(path + "/hello.csv", "w+")    #csv는 엑셀, w는 write
#file.write("hello" + "\n")
#file.write("bye")

file = open("./hello.csv","w+")
file.write("hello" + "\n")
file.write("bye"+"\n")
