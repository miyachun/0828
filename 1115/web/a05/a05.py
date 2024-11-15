import json,urllib.request
from flask import Flask, render_template,request
from urllib.request import urlopen
from bs4 import BeautifulSoup


app = Flask(__name__)
finalAns={}

@app.route('/')
def index():
    global finalAns
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
   

    return render_template('index.html',data=finalAns)

@app.route('/findA', methods = ['POST'])
def findA():
    dropdownval = request.form.get('colour')
    print(dropdownval)

    return render_template('index.html',data=finalAns,d=dropdownval,da=finalAns[dropdownval])


if __name__ == '__main__':
    app.run()