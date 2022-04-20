
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/Livyatan').read()
#print(source)

soup = BeautifulSoup(source,'lxml')

list_1 = []
for paragraph in soup.find_all('span', class_="mw-headline"):
    list_1.append(paragraph.text)
    
print(list_1)


"""
import requests
from bs4 import BeautifulSoup
html = requests.get("https://en.wikipedia.org/wiki/Livyatan")
soup = BeautifulSoup(html.text, "html.parser")
metadata = soup.find_all('p')

out = ""
for paragraph in metadata:
    out += paragraph.text

print(out)
"""