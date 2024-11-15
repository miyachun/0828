from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://rate.bot.com.tw/xrt?Lang=zh-TW')
bs = BeautifulSoup(html.read(), 'html.parser')

title =bs.find_all("div", {"class":"visible-phone print_hide"})
results = bs.select('td[data-table="本行現金賣出"]')
content=bs.find_all(results, {"class":"rate-content-cash text-right print_hide"})

linktitle=[]
linkcontent=[]
for l in title:
    l = l.decode_contents().strip()
    linktitle.append(l)
#print(len(linktitle))
#print(linktitle)

for l in results:
    #l = l.decode_contents().strip()
    linkcontent.append(l.get_text())
finalAns=dict(zip(linktitle,linkcontent[::2]))
print(finalAns)
print(type(finalAns))

print('查詢:0->美金，1->港幣')
a=input('輸入:')
if a=='0':
    print(finalAns['美金 (USD)'])
elif a=='1':
    print(finalAns['港幣 (HKD)'])


    



