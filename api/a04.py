import json,urllib.request
import re

url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/5ae41ecf-1ea0-420d-acbf-90c59cedf999?format=json'

data = urllib.request.urlopen(url).read()
output = json.loads(data)
location=output['result']['records']


for i in location:
    city = i['Name']
    strT=i['Start']
    endT=i['End']
    a=strT+city
    #FstrT=re.compile(r'(\d\d\d\d)/(\d\d)/(\d\d)')
    #result=FstrT.findall(a)
    FstrT=re.compile(r"[\u4E00-\u9FA5]{2,1000}")
    result=FstrT.search(a)
    
 
    
    #for item in result:
    #    print (item)
    print(result)