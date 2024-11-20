import json,urllib.request
from flask import Flask, render_template
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD={'area':[],'name':[],'addr':[],'tel':[]}
  
@app.route('/')
def index():
    
    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/8fd11d4a-e389-4526-9fc5-6674108b0f5e?format=json'

    data = urllib.request.urlopen(url).read()
    
    output = json.loads(data)
    location=output['result']['records']
   
    for i in location:
        #print(i)
        area = i['特約服務區域']        
        name=i['單位名稱']
        addr=i['地址']
        tel=i['聯絡電話']
        #a=strT+city
        myD['area'].append(area)
        myD['name'].append(name)
        myD['addr'].append(addr)
        myD['tel'].append(tel)
        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()