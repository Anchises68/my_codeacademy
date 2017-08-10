
import requests
from bs4 import BeautifulSoup, Tag

source = requests.get('https://www.familyfriendpoems.com/print/poem/NDA2MDE=')


response = source.content
soup = BeautifulSoup(response, 'html.parser')

tag = soup.find_all('p') + soup.find_all('script') + soup.find_all('b') + soup.find_all('title') + soup.find_all('a')
for i in tag:
    i.decompose()
print (soup.get_text())
print (soup.prettify())


