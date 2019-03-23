from urllib.request import urlopen
import urllib.request
import bs4


url = "http://www.pknu.ac.kr/index.do"
html = urlopen(url)
#print(html.read())
data = bs4.BeautifulSoup(html,"html.parser")
notice_box = data.find("div",{"id":"tab3"})
part_notice_box = notice_box.findAll("li",{"class":"issue"})
for div_finding in part_notice_box:
    div = div_finding.find("div",{"class":"subject"})
    #print(div)
    subject = div.find("a").text
    print(subject)
