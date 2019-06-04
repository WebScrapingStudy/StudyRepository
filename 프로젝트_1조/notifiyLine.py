import requests
import bs4
import time

def send_notifiy(repeat=True, idle=30):
    """
    보안뉴스 속보정보를 갱신하여 새롭게 추가된 속보를
    라인 노티파이에 연결해서 사용자에게 메세지로 전달
    리눅스 cron 혹은 윈도우 작업스케쥴러를 이용하여 실행가능하며
    데몬프로세스로 백그라운드에서 동작가능한 함수이다.
    :param repeat: 반복 실행여부 체크 (데몬프로세스로 실행시 True)
    :param idle: 반복 시간 설정 (분)
    :return: None
    """
    TARGET_URL = "https://notify-api.line.me/api/notify"
    try:
        f = open("token.txt", 'r')
        a = f.read()
        f.close()
        token_list = a.split(' ')[:-1]
    except:
        print("Need token.txt")
        exit(1)

    while True:
        res = requests.get('https://www.boannews.com/Default.asp')
        bs_obj = bs4.BeautifulSoup(res.text,"html.parser")
        article = bs_obj.find("article",{"class":"fast_news"})
        lis = article.find_all("li")

        fast_list = []
        for li in lis:
            fast_list += [li.a.attrs.get('href').split('idx=')[1]]

        try:
            f = open("last.txt", 'r')
            a = f.read()
            f.close()
            last_list = a.split(' ')[:-1]
        except:
            last_list = []

        f = open("last.txt", 'w')
        for i in range(0, 10):
            data = fast_list[i] +' '
            f.write(data)
        f.close()

        send_list = [li for li in fast_list if li not in last_list]

        if len(send_list) > 0:
            message = ''
            for link in send_list:
                message += 'https://www.boannews.com/media/view.asp?idx=' + link + '\n'
            for token in token_list:
                requests.post(TARGET_URL, headers={'Authorization': 'Bearer ' + token},data={'message': message})

        time.sleep(idle*60)
        if repeat is False:
            break;
if __name__ == '__main__':
    send_notifiy(False,0)

