import json,urllib.request
from flask import Flask, render_template,request
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'name':[],'addr':[],'tel':[]}
myR={'name':[],'addr':[]}
myP={'name':[],'info':[]}

@app.route('/restaurant')
def restaurant():
    global myR
    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/c69de83f-0f95-44f9-890a-884ceb65b103?format=json'
    data = urllib.request.urlopen(url).read()    
    output = json.loads(data)
    location=output['result']['records']
    for i in location:
        #print(i)
        name = i['友善空間名稱']        
        addr=i['地址']
        
        myR['name'].append(name)
        myR['addr'].append(addr)

    return render_template('restaurant.html',a=myR)


@app.route('/park')
def park():
    global myP

    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/868af070-974e-4c11-bf1f-c7b78e2e10db?format=json'
    data = urllib.request.urlopen(url).read()    
    output = json.loads(data)
    location=output['result']['records']
                
    for i in location:
        #print(i)
        name = i['公園名稱']
        info=i['設施']
        
        #a=strT+city
        myP['name'].append(name)
        myP['info'].append(info)
        
    return render_template('park.html',a=myP)





@app.route('/')
def index():
    global myD

    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/c3f12332-0515-444e-a7aa-cf3d4ad4d1f3?format=json'
    data = urllib.request.urlopen(url).read()    
    output = json.loads(data)
    location=output['result']['records']

    for i in location:
        #print(i)
        name = i['名稱']
        addr=i['地址']
        tel=i['公務電話']
        #a=strT+city
        myD['name'].append(name)
        myD['addr'].append(addr)
        myD['tel'].append(tel)
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()