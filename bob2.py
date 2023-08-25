from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date
import re

today = date.today().strftime("%Y/%m/%d")

html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/breakfast")
soup = BeautifulSoup(html, "html.parser")
breakfast = re.sub("<[^<>]*>", "", str(soup.select(".ulType_food > li:nth-child(2) > dl > dd")[0]).replace("<br/>", "\n"))

html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html, "html.parser")
lunch = re.sub("<[^<>]*>", "", str(soup.select(".ulType_food > li:nth-child(2) > dl > dd")[0]).replace("<br/>", "\n"))

html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/dinner")
soup = BeautifulSoup(html, "html.parser")
dinner = re.sub("<[^<>]*>", "", str(soup.select(".ulType_food > li:nth-child(2) > dl > dd")[0]).replace("<br/>", "\n"))

print("===================================================")
print(breakfast)
print("===================================================")
print(lunch)
print("===================================================")
print(dinner)
print("===================================================")
