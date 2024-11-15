import json,urllib.request
from flask import Flask, render_template,request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)  


@app.route('/')
def index():
    url = 'https://water.taiwanstat.com/'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    reservoir = soup.select('.reservoir')
    x=[]
    y=[]
    finalAns={}
    for i in reservoir:
        #print(i.find('div', class_='name').get_text(), end=' ')
        #print(i.find('h5').get_text(), end=' ')
        x.append(i.find('div', class_='name').get_text(strip=True))
        y.append(i.find('h5').get_text(strip=True))
      
       
    finalAns={'city':x,'n':y}

    return render_template('index.html',data=finalAns)



if __name__ == '__main__':
    app.run()