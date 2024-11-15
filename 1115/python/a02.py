from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.lhu.edu.tw/')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
