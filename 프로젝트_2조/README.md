# 프로젝트 2조
## 부경대학교 수강신청 매크로
### 팀원
* 이선경 
* 전호범  
### 사용방법
1. 환경설정
`pip install pyautogui`

2. 설정파일 확인 config.py  
자동로그인기능 활성화 `login_funtion=True`  
id와 pw 기입  
로그인 미사용시 로그인된 상태에서 진행
3. 학수번호 입력 course.txt  
수강신청할 학수번호를 기입  
띄어쓰기를 이용하여 구분  

4. [수강신청](https://sugang.pknu.ac.kr) 인터넷 창 실행  
모든 컨텐츠 보기 클릭  
빨간 수강신청버튼 클릭 로그인 창에서 프로그램 실행

5. 프로그램 실행 `python run.py`

6. 종료  
마우스 커서를 화면의 왼쪽 위 모서리(x=0, y=0)로 이동

### How to use
1. Requirements install using
`pip install pyautogui`  

2. config.py  
Set `login_funtion=True` 
check id and pw  
if `login_funtion=False` you should login

3. course.txt  
insert your course number  
split using `\n`  

4. run Internet Explorer [sugangpage](https://sugang.pknu.ac.kr) 

5. run module using `python run.py`  

6. Stop using goto mouse cursor left-top(x=0,y=0)

### Errors
* 2019.08.08 Login 주기를 4분으로 설정하면 로그아웃 직후에 로그인됩니다.
* btn error  
버튼 에러 발생시 btn폴더안에 있는 버튼을 보시고  
캡처 도구를 이용하여 버튼들을 캡처해서 같은이름으로 덮어쓰기 해주세요  
make button image using capture tool  
Be careful when saving file names  

#### Test Environment
* Display 27inch, FHD(1920x1080)  
버튼의 해상도에 따라 좌표인식이 안 될 가능성이 있습니다.
* python 3.7
* pyautogui 0.9.47

#### Reperence
* [pyautogui](https://wikidocs.net/26460#_8)