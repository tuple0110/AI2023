from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://news.daum.net/breakingnews/digital")

soup = BeautifulSoup(html, "html.parser")
news = soup.select(".tit_thumb > a")
n = 0
for new in news[:10]:
    url = new.get("href") # <a href="https://n.news.naver.com/mnews/article/031/0000767382?sid=105"
    new = new.text.strip()
    if new != "":
        n += 1
    print( "{:02d}".format(n), new)
    print( " ", url)
