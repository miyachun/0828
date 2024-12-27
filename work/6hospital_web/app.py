import json,urllib.request
from flask import Flask, render_template,request
import json,urllib.request



app = Flask(__name__)
myD={'area':[],'name':[],'addr':[],'tel':[]}
myD01={'area':[],'name':[],'addr':[],'tel':[]}

myH={'area':[],'name':[],'addr':[],'tel':[]}


@app.route('/hospital',methods=('GET','POST'))
def hospital():
    url = open('283a5dfa-44e9-4300-8a7f-22e58ecdf7b1.json','r',encoding="utf-8")       
    data = json.load(url) 
    location=data['result']['records']
    for i in location:
        #print(i)
        area = i['縣市']        
        name=i['機構名稱']
        addr=i['地址']
        tel=i['電話']

        
        #a=strT+city
        myH['area'].append(area)
        myH['name'].append(name)
        myH['addr'].append(addr)
        myH['tel'].append(tel)

    return render_template('hospital.html',a=myH)








@app.route('/',methods=('GET','POST'))
def index():
    global myD
    global myD01      

    #url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/2cb206f2-3fb2-42d9-9820-f3291f6bc35c?format=json'
    #data = urllib.request.urlopen(url).read()
    url = open('2cb206f2-3fb2-42d9-9820-f3291f6bc35c.json','r',encoding="utf-8")       
    data = json.load(url)     
    
    location=data['result']['records']
    if request.method == 'POST':
        
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
                        
        return render_template('index.html',a=myD,b=myD01,c='0')
    else:
               
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
        return render_template('index.html',a=myD,b=myD01,c='1')


if __name__ == '__main__':
    app.run()