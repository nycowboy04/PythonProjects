import requests
import bs4

res=requests.get('https://en.wikipedia.org/wiki/Cicada_3301')
soup=bs4.BeautifulSoup(res.text,'lxml')
image_info=soup.select('.thumbimage')
cicada=image_info[0]
image_link='http:'+cicada['src']
cicada_image=requests.get(image_link,'lxml')
f=open('cicada_image_new.jpg','wb')
f.write(cicada_image.content)
f.close()
