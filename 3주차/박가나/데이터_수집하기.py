from gn_lib3.naver_api_caller import get1000Result
import json

list = []
result1 = get1000Result("부경대 맛집")
result2 = get1000Result("해운대 맛집")
list = list + result1 + result2

file = open("./famous_restaurant.json", "w+")
file.write(json.dumps(list))
