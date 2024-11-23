import json,urllib.request
from flask import Flask, render_template,request
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'web':[],'name':[]}
myR={'name':[],'tel':[],'addr':[]}
myP={'web':[],'name':[]}

@app.route('/restaurant')
def restaurant():
    global myR
    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/756106eb-9dda-4bde-a5b7-e0659685e7eb?format=json'
    data = urllib.request.urlopen(url).read()    
    output = json.loads(data)
    location=output['result']['records']
    for i in location:
        #print(i)
        name = i['餐廳名稱']        
        tel=i['餐館電話']
        addr=i['餐館地址']
        myR['name'].append(name)
        myR['tel'].append(tel)
        myR['addr'].append(addr)

    return render_template('restaurant.html',a=myR)


@app.route('/play')
def play():
    global myP

    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/eae89760-4779-4bc6-9933-816d43ae9016?format=json'
    data = urllib.request.urlopen(url).read()    
    output = json.loads(data)
    location=output['result']['records']
                
    for i in location:
        #print(i)
        web = i['TYWebsite']
        name=i['Name']
        
        
        #a=strT+city
        myP['web'].append(web)
        myP['name'].append(name)
        
    return render_template('play.html',a=myP)





@app.route('/')
def index():
    global myD

    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/5ae41ecf-1ea0-420d-acbf-90c59cedf999?format=json'
    data = urllib.request.urlopen(url).read()    
    output = json.loads(data)
    location=output['result']['records']

    for i in location:
        #print(i)
        web = i['TYWebsite']
        name=i['Name']

        myD['web'].append(web)
        myD['name'].append(name)

    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()