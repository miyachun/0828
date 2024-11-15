import requests
from bs4 import BeautifulSoup

url = 'https://water.taiwanstat.com/#reservoir1'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
reservoir = soup.select('.reservoir')
for i in reservoir:
  print(i.find('div', class_='name').get_text(), end=' ')
  print(i.find('h5').get_text(), end=' ')
  print()