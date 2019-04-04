from lib.naver_api_caller import get1000Result
import json
#result = caller.call("대연동 맛집", 1) #몇번부터 시작할지, 100개씩

#for num in range(0,10):
#    print(caller.call("남천동 맛집",num*100+1))
#    #print(caller.call("감만동 맛집",101))


#굳이 json파일로 만드는 이유? 데이터 분석을 하기 위해 Pandas를 사용할것인데, 그때 사용을 편하게 하기위하여 json 파일로 변환을 해주는 것이다.
result = get1000Result("대연동 맛집")
result2 = get1000Result("대연동 카페")
list = list + result + result2

file = open("./daeyeon.json", "w+")
file.write(json.dumps(list))
#json.dumps(list)
#print(len(list))
