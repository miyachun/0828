import requests

url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
rate = requests.get(url)
rate.encoding = 'utf-8'
rt = rate.text
rts = rt.split('\n')

for i in rts:
    try:
        a = i.split(',')
        print(a[0] + ': ' + a[12])
    except:
      break