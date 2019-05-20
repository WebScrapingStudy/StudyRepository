from bs4 import BeautifulSoup
import requests


class boann(object):
    base_url = "https://www.boannews.com/"

    def __init__(self):
        pass

    def vulnerability(self):
        url = "media/s_list.asp?skind=5"
        res = requests.get(self.base_url+url)
        soup = BeautifulSoup(res.text,"html.parser")
        news = soup.find_all("div",{"class":"news_list"})
        news[0].a.text.split('\n')[2]
        message = self.base_url+news[0].a.attrs.get('href') +" "+ self.base_url+news[1].a.attrs.get('href')
        return message

    def 속보(self):
        message = ""
        return message

    def search(self,keyword):
        message = ""
        return  message