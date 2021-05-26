from urllib.request import urlopen
import random
from bs4 import BeautifulSoup
from urllib.request import Request


def lightshot(content):
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
    return sendImg
