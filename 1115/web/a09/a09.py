import json,urllib.request
from flask import Flask, render_template,request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def fA(info):
    url = 'https://tw.stock.yahoo.com/quote/'+info+'.TW'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.select('.Fw\(b\)')[0]
    a = soup.select('.Fz\(32px\)')[0]
    b = soup.select('.Fz\(20px\)')[0]
    s = ''
    print(url)
    try:

        if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-down\)')[0]:
            s = '-'
    except:
                try:

                    if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-up\)')[0]:
                        s = '+'
                except:

                    s = '-'
    a=[title.get_text(),a.get_text(),s,b.get_text()]

    #print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )')
    return a


@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST': 
        # Retrieve the text from the textarea 
        text = request.form.get('textarea') 
  
        # Print the text in terminal for verification 
        print(text) 
  
        return render_template('index.html',data=fA(text))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()