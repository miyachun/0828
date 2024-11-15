from urllib.request import urlopen
from bs4 import BeautifulSoup


def fA(url):
    linkcontent=[]
    f=[]
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')

    

    title =bs.find_all("div", {"class":"col-12 mb-3"})
        
    n0 = title[0].getText()
    n1 = title[1].getText()
    f0 = title[2].getText()
    f1 = title[3].getText()
    f2 = title[4].getText()
        

    print(n0)
    print(n1)
    print(f0)
    print(f1)
    print(f2)


url5='https://www.etax.nat.gov.tw/etw-main/ETW183W2_11305/'
url3='https://www.etax.nat.gov.tw/etw-main/ETW183W2_11303/'
url1='https://www.etax.nat.gov.tw/etw-main/ETW183W2_11301/'
print('查詢:按1->(1月-2月)，按2->(3月-4月),按3->(5月-6月)')
a=input('輸入:')
if a=='1':
    fA(url1)
elif a=='2':
    fA(url3)
elif a=='3':
    fA(url5)
