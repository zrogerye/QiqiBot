from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request
from lxml import html
import requests
import random

# https://rule34.xxx/index.php?page=post&s=random
# https://rule34.xxx/index.php?page=post&s=view&id=4758442
# https://rule34.xxx/index.php?page=post&s=list&tags=1girls





url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags=sex'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req).read()
soup = BeautifulSoup(html_page, features="html.parser")
#soup.findAll('https://us.rule34.xxx/images/')
split = str(soup).split()
#print(split)
images = []
for img in split:
    s = img
    if(s.startswith('file_url')):
        images.append(s)

finImages = []
for imgF in images:
    f = imgF
    i = f[10:len(f)-1]
    finImages.append(i)

fin = random.choice(finImages)
print(fin)



# rule34
#req = Request('https://rule34.xxx/index.php?page=post&s=random', headers={'User-Agent': 'Mozilla/5.0'})
#html_page = urlopen(req).read()
#soup = BeautifulSoup(html_page, features="html.parser")
#print(soup)
#sendImg = None
#for img in soup.findAll('img'):
#    s = img.get('src')
#    if (s.startswith("https://us.rule34.xxx")):
#        sendImg = s
#print(sendImg)