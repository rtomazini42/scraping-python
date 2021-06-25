from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
#response = urlopen('https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number')
try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    #print(response.read())

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

#html = response.read().decode('utf-8')
soup = BeautifulSoup(response, 'html.parser')
#result = soup.findAll('tr')
result = soup.findAll('td')
for resultado in result:
    link = resultado.find("a")
    if (link != None):
        link = link.get_text()
        print(link)
    else:
        print()
#result = result.findAll('title')
#print(result)
print("teste")
