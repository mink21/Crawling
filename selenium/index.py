from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("newFile.txt", 'w')
for anchor in soup.select("a.nav"):
    data = str(i) + "위: " + anchor.get_text() + "\n"
    i += 1
    f.write(data)
f.close()
