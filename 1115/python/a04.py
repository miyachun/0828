from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://rate.bot.com.tw/xrt?Lang=zh-TW')
bs = BeautifulSoup(html.read(), 'html.parser')


title =bs.find_all("div", {"class":"visible-phone print_hide"})


for element in title:
    print(element.decode_contents().strip())
