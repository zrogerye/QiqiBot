import discord
import smtplib
from email.mime.text import MIMEText
import os
from rule34 import rule34
from voicelines import voicelines
from sendmail import sendemail
from lightshotRandom import lightshot

# keepAlive is used for hosting on replit
# from keepAlive import keepAlive

client = discord.Client()
TOKEN = 'insert token here'


@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))


@client.event
async def on_message(message):
    content = message.content.lower()

    # tbh no idea what this is for
    if message.author == client.user:
        return

    # to email people
    if message.content.startswith('>email'):
        out = sendemail(content)
        await message.channel.send(out)

    # qiqi says hello
    if message.content.startswith('>hello'):
        await message.channel.send('I am Qiqi. I am a zombie. I forgot what comes next.')

    # qiqi says a voiceline
    if message.content.startswith('>qiqi'):
        out = voicelines(content)
        await message.channel.send(out)

    # detects if 'ganyu' is in message
    if 'ganyu' in content:
        await message.channel.send('Did someone say Ganyu? Is Ganyu here? Qiqi would like some cocomilk please!')

    # returns a list of commands
    if message.content.startswith('>help'):
        helpMessage = (
            ">help - qiqi will help! \n>hello - says hi to me, Qiqi! \n>qiqi - qiqi will say something cool \n>email "
            "- >email/receiver's email/subject/message/qiqi 1 or qiqi 2 \nganyu - is cocogoat here? ")
        await message.channel.send(helpMessage)

    # rule34
    if message.content.startswith('>r34'):
        out = rule34(content)
        if out != 'qiqi could not find any images with that tag':
            await message.channel.send((' <' + out + '>'))
        await message.channel.send(out)

    # random lightshot image
    if message.content.startswith('>lightshot') or message.content.startswith('>ls'):
        out = lightshot()
        await message.channel.send(out)

    # spam email
    if message.content.startswith('>spamemail'):
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
        while count < int(args[2]):
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

    # beyblades idk man
    if message.content.startswith('>beyblades'):
        bey = 'Beyblade, Beyblade \nLet it rip! \nLets Fight an epic Battle, \nFace off, and spin the metal,' \
              '\nNo time for doubt now, no place for backing down,\nBeyblade, Beyblade\nLet it rip!\nBeyblade, ' \
              'Beyblade\nLet it rip!\nSpin out, your bey now, bring on, the power!\nRight to the top yeah, ' \
              'Were never giving up!\nHere it comes Here it comes... Metal Fusion!\nLets go Beyblade,' \
              '\nLet it rip!\nMetal Fusion, Let it rip!\nBeyblade, Beyblade\nLet it rip!\nThis is it, Get a grip, ' \
              'Let it rip! '
        await message.channel.send(bey)


# keepAlive()
client.run(TOKEN)
