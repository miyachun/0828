import json,urllib.request
from flask import Flask, render_template,request
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'area':[],'name':[],'addr':[],'tel':[]}
myD01={'area':[],'name':[],'addr':[],'tel':[]}
c='1'
@app.route('/',methods=('GET','POST'))
def index():
    global myD
    global myD01
    global c   

    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/2cb206f2-3fb2-42d9-9820-f3291f6bc35c?format=json'

    data = urllib.request.urlopen(url).read()
    
    output = json.loads(data)
    location=output['result']['records']
    if request.method == 'POST':
        c='0'
        myD01.clear()
        myD01={'area':[],'name':[],'addr':[],'tel':[]} 
        dropdownval=request.form.get('colour')
        print(dropdownval)
        for i in location:
            #print(i)
            area = i['區域']        
            name=i['藥局名稱']
            addr=i['地址']
            tel=i['電話']
            #a=strT+city
            myD['area'].append(area)
            myD['name'].append(name)
            myD['addr'].append(addr)
            myD['tel'].append(tel)        
            if dropdownval in area:
                myD01['area'].append(area)
                myD01['name'].append(name)
                myD01['addr'].append(addr)
                myD01['tel'].append(tel)
                        
        return render_template('index.html',a=myD,b=myD01,c=c)
    else:
        myD01.clear()       
        for i in location:
            #print(i)
            area = i['區域']        
            name=i['藥局名稱']
            addr=i['地址']
            tel=i['電話']
            #a=strT+city
            myD['area'].append(area)
            myD['name'].append(name)
            myD['addr'].append(addr)
            myD['tel'].append(tel)
        return render_template('index.html',a=myD,b=myD01,c=c)


if __name__ == '__main__':
    app.run()