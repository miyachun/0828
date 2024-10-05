
import requests


x = requests.get('https://www.lhu.edu.tw/')


print(x.text)