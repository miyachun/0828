import requests
from bs4 import BeautifulSoup

def fA(info):
    url = 'https://tw.stock.yahoo.com/quote/'+info+'.TW'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    #title = soup.find('h1')
    title = soup.select('.Fw\(b\)')[0]
    a = soup.select('.Fz\(32px\)')[0]
    b = soup.select('.Fz\(20px\)')[0]
    s = ''

    try:

        if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-down\)')[0]:
            s = '-'
    except:
                try:

                    if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-up\)')[0]:
                        s = '+'
                except:

                    s = '-'

    print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )')
print('輸入股票號碼:')
a=input('輸入:')
fA(a)

