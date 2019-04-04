import requests
from urllib.parse import urlparse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

keyword = "디퓨저"

url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                                headers={"X-Naver-Client-Id":"ySCz5OuCJACZLZI3wb53",
                                        "X-Naver-Client-Secret":"1tx3ssiGk4"})
json_obj = result.json()
print(result.json())
