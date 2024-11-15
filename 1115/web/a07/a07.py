import json,urllib.request
from flask import Flask, render_template,request
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

def fA(url):
    global a
    global finalAns
    html = urlopen(url)
    bs= BeautifulSoup(html.read(), 'html.parser')   
    a=[]
    finalAns={}
    title =bs.find_all("div", {"class":"col-12 mb-3"})
    
    n0 = title[0].getText(strip=True)
    n1 = title[1].getText(strip=True)
    f0 = title[2].getText(strip=True)
    f1 = title[3].getText(strip=True)
    f2 = title[4].getText(strip=True)
    a.append(f0)
    a.append(f1)
    a.append(f2)
    
    finalAns={'特別獎':n0,'特獎':n1,'頭獎':a}
    
    print(a)
    return finalAns
    

@app.route('/')
def index():
    url5='https://www.etax.nat.gov.tw/etw-main/ETW183W2_11305/'
    url3='https://www.etax.nat.gov.tw/etw-main/ETW183W2_11303/'
    url1='https://www.etax.nat.gov.tw/etw-main/ETW183W2_11301/'


    return render_template('index.html',data=fA(url1))


if __name__ == '__main__':
    app.run()