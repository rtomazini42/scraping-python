from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


url = "https://en.wikipedia.org/wiki/List_of_even-toed_ungulates_by_population"

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    #print(response.read())

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

soup = BeautifulSoup(response, 'html.parser')
tabela =soup.findAll("table",{"class": "wikitable"})

cards = []
for item in tabela:
    print(item.get_text())
    cards.append(item.get_text())
