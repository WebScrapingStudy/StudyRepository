'''9강'''
import urllib.request               #urllib에 request한다.

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)  #urlopen이라는 function을 호출

print(html.read())                  

'''10강'''
