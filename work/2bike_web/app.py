import json,urllib.request
from flask import Flask, render_template,request,url_for, flash, redirect, abort
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_bootstrap import Bootstrap


app = Flask(__name__)
myD={'sarea':[],'name':[],'addr':[],'total':[],'now':[]}

myD01={'areaName':[],'parkName':[],'address':[],'totalSpace':[],'surplusSpace':[]}

@app.route('/login')
def login():   
    url = open('0381e141-f7ee-450e-99da-2240208d1773.json','r',encoding="utf-8")       
    data = json.load(url) 
    
    
    location=data['result']['records']
   
    for i in location:
        #print(i)
        areaName=i['areaName']
        parkName = i['parkName']
        address=i['address']
        totalSpace=i['totalSpace']               
        surplusSpace=i['surplusSpace']
        
        
        #a=strT+city
        myD01['areaName'].append(areaName)
        myD01['parkName'].append(parkName)
        myD01['address'].append(address)        
        myD01['totalSpace'].append(totalSpace)
        myD01['surplusSpace'].append(surplusSpace)
        
    return render_template('list.html',a=myD01)




@app.route('/')
def index():
    
    

    url = open('a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f.json','r',encoding="utf-8")       
    data = json.load(url)
    
    
    location=data['result']['records']
   
    for i in location:
        #print(i)
        sarea=i['sarea']
        name = i['sna']
        addr=i['ar']               
        total=i['tot']
        now=i['sbi']
        
        #a=strT+city
        myD['sarea'].append(sarea)
        myD['name'].append(name)
        myD['addr'].append(addr)        
        myD['total'].append(total)
        myD['now'].append(now)
        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()