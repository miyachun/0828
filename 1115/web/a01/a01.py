import json,urllib.request
from flask import Flask, render_template
import requests

app = Flask(__name__)

a0=[]
a12=[]    
@app.route('/')
def index():
    global a0
    url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
    rate = requests.get(url)
    rate.encoding = 'utf-8'
    rt = rate.text
    rts = rt.split('\n')
    for i in rts:
        try:
            a = i.split(',')
            print(a[0] + ': ' + a[12])
            a0.append(a[0])
            a12.append(a[12])
        except:
            break
    return render_template('index.html',a=a0,b=a12)


if __name__ == '__main__':
    app.run()