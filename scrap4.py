from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


url = "https://papers.co/"

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    #print(response.read())

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

#html = response.read().decode('utf-8')
soup = BeautifulSoup(response, 'html.parser') #.decode('utf-8')
soup = soup.findAll("img")
for item in soup:
    a = item
    print(a)
