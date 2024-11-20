#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
import json,urllib.request
import time

API_KEY='XXXX'
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization='+API_KEY


def getquk():
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['records']['Earthquake'][0]['ReportContent']
    #print(location)
    return location


buff = None


while True:    
    qdata = getquk()    
    if qdata != buff:        
        print(qdata)    
    buff = qdata    
    time.sleep(100)
