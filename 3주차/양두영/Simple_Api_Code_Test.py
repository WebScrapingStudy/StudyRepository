import requests
from urllib.parse import urlparse

keyword="술"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result =requests.get(urlparse(url).geturl(),headers={"X-Naver-Client-Id":"J0lOZ8gLyxgJYZED5qXt",
                                                    "X-Naver-Client-Secret":"bWEyy4p0NJ"})
json_obj=result.json()
print(json_obj)