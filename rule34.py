from urllib.request import urlopen
import random
from bs4 import BeautifulSoup
from urllib.request import Request


def rule34(content):
    temp = True
    args = content.split(' ')

    if len(args) == 1:
        temp = False
        req = Request('https://rule34.xxx/index.php?page=post&s=random', headers={'User-Agent': 'Mozilla/5.0'})
        html_page = urlopen(req).read()
        soup = BeautifulSoup(html_page, features="html.parser")
        sendImg = None
        for img in soup.findAll('img'):
            s = img.get('src')
            if s.startswith("https://us.rule34.xxx"):
                sendImg = s
        return sendImg
        # await message.channel.send('<' + sendImg + '>')

    if temp == True:
        url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags='
        tag = args[1]
        url += tag
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_page = urlopen(req).read()
        soup = BeautifulSoup(html_page, features="html.parser")
        split = str(soup).split()
        images = []
        for img in split:
            s = img
            if s.startswith('file_url'):
                images.append(s)

        finImages = []
        for imgF in images:
            f = imgF
            i = f[10:len(f) - 1]
            finImages.append(i)

        if len(finImages) == 0:
            temp = False
            return 'qiqi could not find any images with that tag'

        if temp == True:
            fin = random.choice(finImages)
            return fin
            # await message.channel.send('<' + fin + '>')
