from bs4 import BeautifulSoup
import requests


class boann(object):
    base_url = "https://www.boannews.com/"

    def __init__(self):
        pass

    def vulnerability(self):
        """
        취약점
        :return:
        """
        url = "media/s_list.asp?skind=5"
        res = requests.get(self.base_url+url)
        soup = BeautifulSoup(res.text,"html.parser")
        news = soup.find_all("div",{"class":"news_list"})
        a=self.base_url+news[0].a.attrs.get('href').split('&')[0]
        b=self.base_url+news[1].a.attrs.get('href').split('&')[0]
        c=self.base_url+news[2].a.attrs.get('href').split('&')[0]
        return a+"\n"+b+"\n"+c

    def All_News(self):
        """
        전체기사
        :return: 
        """
        url = "media/t_list.asp"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def securityworld(self):
        """
        시큐리티월드
        :return: 
        """
        url = "securityworld/"
        mes = ''
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find("div", {"id": "head1"})
        a = self.base_url + news.a.attrs.get('href').split('&')[0]
        news = soup.find("div", {"id": "head2"})
        b = self.base_url + news.a.attrs.get('href').split('&')[0]
        mes = a + "\n" + b
        return mes

    def ransomware(self):
        """
        랜섬웨어
        :return: 
        """
        url = "search/news_list.asp?search=title&find=%B7%A3%BC%B6%BF%FE%BE%EE"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def AI(self):
        """
        인공지능(AI)
        :return:
        """
        url = "search/news_list.asp?search=title&find=%C0%CE%B0%F8%C1%F6%B4%C9"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def security(self):
        """
        시큐리티
        :return: 
        """
        url = "media/list.asp?mkind=1"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_main_title"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def event(self):
        """
        사건사고
        :return:
        """
        url = "search/news_list.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def IT(self):
        """
        IT
        :return:
        """
        url = "media/list.asp?mkind=2"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def SAFETY(self):
        """
        SAFETY
        :return:
        """
        url = "media/list.asp?mkind=4"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def international(self):
        """
        국제
        :return:
        """
        url = "media/list.asp?skind=D"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def pub(self):
        """
        공공, 정책
        :return:
        """
        url = "media/list.asp?skind=6"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def interview(self):
        """
        인터뷰, 오피니언
        :return:
        """
        url = "media/list.asp?skind=3"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c

    def weekend(self):
        """
        주말판
        :return:
        """
        url = "search/news_list.asp?search=title&find=%C1%D6%B8%BB%C6%C7"
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c
    def search(self,keyword):
        """
        검색
        :return:
        """
        from urllib import parse
        keyword = parse.quote(keyword,encoding='EUC-KR')
        print(keyword)
        url = "search/news_list.asp?search=key_word&find="+keyword
        res = requests.get(self.base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("div", {"class": "news_list"})
        a = self.base_url + news[0].a.attrs.get('href').split('&')[0]
        b = self.base_url + news[1].a.attrs.get('href').split('&')[0]
        c = self.base_url + news[2].a.attrs.get('href').split('&')[0]
        return a + "\n" + b + "\n" + c
