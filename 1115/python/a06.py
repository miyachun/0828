import requests
url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url)
web.encoding='utf-8'

from bs4 import BeautifulSoup
soup = BeautifulSoup(web.text, "html.parser")
td = soup.select('.container-fluid')[0].select('.etw-tbiggest')
ns = td[0].getText()
n1 = td[1].getText()

n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]
print(ns)
print(n1)
print(n2)