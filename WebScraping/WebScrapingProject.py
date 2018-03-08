'''
This project was designed to find a hidden code in a website using BeautifulSoup
Web Scraping functionality. This project was done as part of a Python
development course in Udemy by Jose Portilla.
'''
#imports
import requests
import bs4

#initial Scraping
res=requests.get('https://www.thegoldbugs.com/blog')
soup=bs4.BeautifulSoup(res.text,'lxml')

source=soup.select('pre') #Found the section we needed via HTML source
source_text=source[0]

#formatting the scraped information
source_string=str(source_text)
split=source_string.split(sep='-----')

#finalizing and formatting the output for the final answer
output=[]
for item in split:
    output+=item[0]
print(''.join(output))
