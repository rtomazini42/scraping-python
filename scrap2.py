

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.alura.com.br'
url = 'https://cursos.alura.com.br/course/web-scraping-data-science-python/task/61709'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    print(response.read())

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
