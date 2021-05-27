from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request
import requests
import random
import urllib.request
import requests


def lightshot():
    url = 'https://prnt.sc/'
    url += str(random.randint(0, 999999))
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, features="html.parser")
    sendImg = None
    for img in soup.findAll('img'):
        s = img.get('src')
        if s.startswith("https://i.imgur.com/"):
            sendImg = s

    if sendImg is None:
        return 'qiqi says this image has committed nonexistence'

    if sendImg is not None:
        url = sendImg
        r = requests.get(url)
        # print(r.url)
        bruh = r.url
        if bruh == 'https://i.imgur.com/removed.png':
            return 'qiqi says this image has committed nonexistence'
        if bruh != 'https://i.imgur.com/removed.png':
            return bruh
