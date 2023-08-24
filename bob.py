from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s")
soup = BeautifulSoup(html, "html.parser")
bap = soup.select(".meal_menu ul li")

print("=" * 50)
menuList = bap[0].text.split()
for i in range(len(menuList)):
    print(f"{i + 1}: {menuList[i]}")
print("=" * 50)
