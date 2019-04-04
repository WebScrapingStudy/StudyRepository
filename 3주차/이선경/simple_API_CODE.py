import requests
from urllib.parse import urlparse
#import urllib.parse
keyword = "분모자당면"
client_id = input("# 아이디 : ")
client_secret = input("# 비밀번호 : ")
#encText = urllib.parse.quote(keyword)
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                      headers = {"X-Naver-Client-Id": client_id,
                                "X-Naver-Client-Secret": client_secret })
json_obj = result.json()
print(json_obj)
#print(result.json())
