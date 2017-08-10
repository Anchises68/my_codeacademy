from markov_python.cc_markov import MarkovChain
import requests
from bs4 import BeautifulSoup, Tag


r = requests.get('https://www.familyfriendpoems.com/print/poem/NDA3ODk=')
response = r.content
soup =BeautifulSoup(response, 'html.parser')
tag = soup.find_all('p') + soup.find_all('script') + soup.find_all('b') + soup.find_all('title') + soup.find_all('a')
for i in tag:
    i.decompose()
markov_input = soup.get_text()
mc = MarkovChain()
mc.add_string(markov_input)
a = mc.generate_text()
b = mc.generate_text()
c = mc.generate_text()
d = mc.generate_text()
print (' '.join(a))
print (' '.join(b))
print (' '.join(c))
print (' '.join(d))
print (markov_input)
