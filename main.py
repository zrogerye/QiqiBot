from urllib.request import urlopen

import discord
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
#from keepAlive import keepAlive
import os
from discord.ext import commands
import re
import json
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request

client = discord.Client()
TOKEN = #token here


@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))


@client.event
async def on_message(message):
    content = message.content.lower()

    QiqiLines = [
        'I am Qiqi. I am a zombie. I forgot what comes next.',
        'Did you ask me something? Sorry... I forgot.',
        'Hold my hand please. This wind could blow me away.',
        'I want to build a snowman. Will you help?',
        'I like coconut milk... But, I dont know what it tastes like.',
        'All of this is because of you. Thank you very much. Can you make me a promise? From now on, please, let me protect you. Do you accept? Yes or no?']

    if message.content.startswith(':beyblades'):
        bey = 'Beyblade, Beyblade \nLet it rip! \nLets Fight an epic Battle, \nFace off, and spin the metal,\nNo time for doubt now, no place for backing down,\nBeyblade, Beyblade\nLet it rip!\nBeyblade, Beyblade\nLet it rip!\nSpin out, your bey now, bring on, the power!\nRight to the top yeah, Were never giving up!\nHere it comes Here it comes... Metal Fusion!\nLets go Beyblade,\nLet it rip!\nMetal Fusion, Let it rip!\nBeyblade, Beyblade\nLet it rip!\nThis is it, Get a grip, Let it rip!'
        await message.channel.send(bey)

    # to email people
    if message.content.startswith(':email'):
        GMAILPASS = #password here
        temp = True
        args = content.split("/")
        receiver = args[1]

        sender = ''

        if len(args) < 5:
            await message.channel.send(
                'qiqi thinks there are not enough arguments')
            temp = False

        if int(args[4]) == 1:
            sender = 'botqiqi2515@gmail.com'

        if int(args[4]) == 2:
            sender = 'qiqibot2515@gmail.com'

        if temp == True:
            subject = args[2]
            bodySend = args[3]
            msg = MIMEText(bodySend, 'html')
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = receiver
            s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
            s.login(user=sender, password=GMAILPASS)
            s.sendmail(sender, receiver, msg.as_string())
            s.quit()
            if temp == True:
                await message.channel.send('okay! qiqi will deliver the message')
        temp = True

    # spam email
    if message.content.startswith(':spamemail'):
        temp = True
        args = content.split("/")
        sender = ''

        receiver = args[1]

        if len(args) < 5:
            await message.channel.send(
                'qiqi thinks there are not enough arguments')
            temp = False

        if int(args[4]) == 1:
            sender = 'botqiqi2515@gmail.com'

        if int(args[4]) == 2:
            sender = 'qiqibot2515@gmail.com'

        count = 0
        while (count < int(args[2])):
            if temp == True:
                subject = count
                bodySend = args[3]
                msg = MIMEText(bodySend, 'html')
                msg['Subject'] = str(subject)
                msg['From'] = sender
                msg['To'] = receiver
                s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
                s.login(user=sender, password=os.getenv('GMAILPASS'))
                s.sendmail(sender, receiver, msg.as_string())
                s.quit()
                if temp == True:
                    await message.channel.send('qiqi has delivered email number ' + str(subject))
                count = count + 1
        temp = True

    # tbh no idea what this is for
    if message.author == client.user:
        return

    # qiqi says hello
    if message.content.startswith(':hello'):
        await message.channel.send('I am Qiqi. I am a zombie. I forgot what comes next.')

    # qiqi says a voiceline
    if message.content.startswith(':qiqi'):
        out = QiqiLines[random.randint(0, len(QiqiLines) - 1)]
        await message.channel.send(out)

    # qiqi makes a ur mom joke!
    # if re.compile('.*\\bn+i+c+e+\\b.*').match(content) != None:
    #  await message.channel.send('ur MOM is nice Ha!')

    # qiqi wonders if ganyu is here
    if ('ganyu') in content:
        await message.channel.send('Did someone say Ganyu? Is Ganyu here? Qiqi would like some cocomilk please!')

    # qiqi returns a help
    if message.content.startswith(':help'):
        helpMessage = (
            ":help - qiqi will help! \n:hello - says hi to me, Qiqi! \n:qiqi - qiqi will say something cool \n:email - :email/receiver's email/subject/message/qiqi 1 or qiqi 2 \nganyu - is cocogoat here? ")
        await message.channel.send(helpMessage)

    #rule34
    if message.content.startswith(':r34'):
        temp = True
        args = content.split('/')

        if len(args) == 1:
            temp = False
            req = Request('https://rule34.xxx/index.php?page=post&s=random', headers={'User-Agent': 'Mozilla/5.0'})
            html_page = urlopen(req).read()
            soup = BeautifulSoup(html_page, features="html.parser")
            sendImg = None
            for img in soup.findAll('img'):
                s = img.get('src')
                if (s.startswith("https://us.rule34.xxx")):
                    sendImg = s
            await message.channel.send(sendImg)

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
                if (s.startswith('file_url')):
                    images.append(s)

            finImages = []
            if len(finImages) == 0:
                temp == False
                await message.channel.send('qiqi could not find any images with that tag')

            if(temp == True):
                for imgF in images:
                    f = imgF
                    i = f[10:len(f) - 1]
                    finImages.append(i)

                    
#keepAlive()
client.run(TOKEN)
