import requests
import bs4

res=requests.get('https://en.wikipedia.org/wiki/Room_641A')
soup=bs4.BeautifulSoup(res.text,'lxml')
selection=soup.select('.mw-headline')
for item in selection:
    print(item.text)
    
