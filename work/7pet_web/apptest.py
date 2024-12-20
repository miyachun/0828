import json
jsonFile = open('c69de83f-0f95-44f9-890a-884ceb65b103.json','r',encoding="utf-8")

myR={'name':[],'addr':[]}


data = json.load(jsonFile)


for i in data['result']['records']:
    name = i['友善空間名稱']        
    addr=i['地址']
    myR['name'].append(name)
    myR['addr'].append(addr)

print(myR)
jsonFile.close()

