from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

cards =[]
card = {}

response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

anuncio = soup.find('div', {'class': 'well card'})

infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')
for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text()

items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
items.pop()
acessorios = []
for item in items:
    acessorios.append(item.getText().replace('► ', ''))
card['items'] = acessorios

import pandas as pd

dataset = pd.DataFrame(card)
dataset = pd.DataFrame.from_dict(card, orient = 'index')
print(dataset)
