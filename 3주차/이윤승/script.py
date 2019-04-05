# Token 정보 가져와서 caffe 글쓰기.. code
#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request
import time
import random
import datetime

from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from urllib.error import HTTPError
from urllib.parse import urlencode

DRIVER_DIR = 'F:\work\chromedriver.exe'

def get_naver_token():
    chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
    chromedriver_path = DRIVER_DIR
    print(chromedriver_path )


    naver_cid = "Ey26Fv8hj86xeUYcKMnA" #내 api cl_id
    naver_csec = "3lIDH2BO2I" #내 api cl_secret
    naver_redirect = "http://127.0.0.1:8080" #서비스 url, callback url이걸로 설정되있음 cmd에서 python -m runserver 8080 하면 돌아감

    driver = webdriver.Chrome(DRIVER_DIR)
    driver.get('https://nid.naver.com/nidlogin.login')

    id = 'IDIDID'  #ID  직접 입력
    pw = 'PWPPWPWPWPW' #비번은 직접 입력
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    # time.sleep(1)
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    # time.sleep(1)

    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
    time.sleep(1)


    state = "REWERWERTATE"

    req_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s&state=%s' % (naver_cid, naver_redirect, state)
    driver.get(req_url)

    time.sleep(1)
    ########################## # XXX: 최초 1회만 반드시 필요하고 이후엔 불필요함

    '''
    driver.find_element_by_xpath('//*[@id="profile_optional_list"]/span/label').click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/button/span').click()
    ##########################
    '''

#여기서 오류남  driver.current_url이 값을 제대로 못받아오고 req_url그대로 남아있음
    redirect_url = driver.current_url
    temp = re.split('code=', redirect_url)
    code = re.split('&state=', temp[1])[0]
    driver.quit()

    print(redirect_url)


    url = "https://nid.naver.com/oauth2.0/token?"
    print(url)

    data = "grant_type=authorization_code" + "&client_id=" + naver_cid   + "&client_secret=" + naver_csec + "&redirect_uri=" + naver_redirect + "'&code=" + code + "&state=" + state
    print(data)

    request = urllib.request.Request(url, data=data.encode("utf-8"))
    request.add_header('X-Naver-Client-Id', naver_cid)
    request.add_header('X-Naver-Client-Secret', naver_redirect)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    token = ''
    if rescode == 200:
        response_body = response.read()
        js = json.loads(response_body.decode('utf 8'))
        token = js['access_token']
    else:
        print("Error Code:", rescode)
        return None

    if len(token) == 0:
        return None
    print(token)
    return token


def naver_cafe_post(subject, content):
    token = get_naver_token()
    time.sleep(1)

    header = "Bearer " + token # Bearer 다음에 공백 추가
    clubid = '29415004'
    menuid = '59'
    url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"

    subject = urllib.parse.quote(subject)
    content = urllib.parse.quote(content)

    data = urlencode({'subject': subject, 'content': content}).encode()
    request = urllib.request.Request(url, data=data)
    request.add_header("Authorization", header)
    try:
        response = urllib.request.urlopen(request)

    except HTTPError as e:
        print("url open failed", e, subject, content)
        return

    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

if __name__ == "__main__":

    subject = "글제목"
    contents = "카페 글내용"
#네이버 로그인 api에서 일단 토큰 받아오는게안됨
    token = get_naver_token()
'''
for id in CID:
    naver_cafe_post(token , subject, contents, id)
    print("done")
'''
