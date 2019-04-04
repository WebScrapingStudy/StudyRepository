#jason
#중괄호로 시작해서 중괄호로 끝난다
# key, value 로 구성되어있다. 값은 여러개를 넣을 수 있음.

#따옴표붙이면 문자형, 안붙으면 그냥 숫자형
{"name":"seongyeong", "age": "32"}
[{"name":"seongyeong","age": 32 }]

#따옴표 세개면 html을 보기좋게 적을 수 있다.
html_str = """
<html>
    <body>
    </body>
</html>
"""


#bs4가 html을 뽑아내는것을 가능하게 해준다.
#html을 비교적 쉽게 다룰 수 있게 해주는 html.parser 기능



#tag <ul></ul><li></li><div></div, and a tag
#property 속성 class, id, href, title, src
#property value 속성값 class = "greet"에서 greet이 속성값
#html <html></html>