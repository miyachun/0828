import json,urllib.request
from flask import Flask, render_template
import requests

import json,urllib.request
import re


app = Flask(__name__)
myD=myD={'city':[],'strT':[],'endT':[]}
  
@app.route('/')
def index():
    global myD
    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/5ae41ecf-1ea0-420d-acbf-90c59cedf999?format=json'

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['result']['records']
    for i in location:
        city = i['Name']
        strT=i['Start']
        endT=i['End']
        a=strT+city
        myD['city'].append(city)
        myD['strT'].append(strT)
        myD['endT'].append(endT)
        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()