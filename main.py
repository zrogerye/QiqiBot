import discord
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from keepAlive import keepAlive
import os
from discord.ext import commands
import re
import json
from twilio.rest import Client

#twilio shit
twilioAccount = os.getenv('TWILIOACCOUNT')
twilioToken = os.getenv('TWILIOTOKEN')
twilioClient = Client(twilioAccount, twilioToken)




#counts how many times each day a person says nice (WIP)
victorDaily = 0
rogerDaily = 0
nathanDaily = 0
jackDaily = 0

client = discord.Client()

#niceCounterFile = open('niceCounter.json', 'r+')
#niceCounterJSON = json.loads(niceCounterFile.read())


victorNiceCounterFile = open('victor.txt', 'r+')
nathanNiceCounterFile = open('nathan.txt', 'r+')
rogerNiceCounterFile = open('roger.txt', 'r+')
jackNiceCounterFile = open('jack.txt', 'r+')

nathan = nathanNiceCounterFile.read()
victor = victorNiceCounterFile.read()
roger = rogerNiceCounterFile.read()
jack = jackNiceCounterFile.read()

#counts how many times total each person says nice11
def update():
  global roger,victor,nathan,jack
  victorNiceCounterFile.seek(0)
  nathanNiceCounterFile.seek(0)
  rogerNiceCounterFile.seek(0)
  jackNiceCounterFile.seek(0)
  roger = (rogerNiceCounterFile.read())
  victor = (victorNiceCounterFile.read())
  nathan = (nathanNiceCounterFile.read())
  jack = (jackNiceCounterFile.read())

def addVictor():
  global victor,victorNiceCounterFile
  victorNiceCounterFile.seek(0)
  oldVictor = victorNiceCounterFile.read().strip()
  newVictor = int(float(oldVictor))
  newVictor = newVictor + 1
  victorNiceCounterFile.truncate(0)
  victorNiceCounterFile.seek(0)
  victorNiceCounterFile.write(str(newVictor))
  update()

def addRoger():
  global roger,rogerNiceCounterFile
  rogerNiceCounterFile.seek(0)
  oldRoger = rogerNiceCounterFile.read().strip()
  newRoger = int(float(oldRoger))
  newRoger = newRoger + 1
  rogerNiceCounterFile.truncate(0)
  rogerNiceCounterFile.seek(0)
  rogerNiceCounterFile.write(str(newRoger))
  update()

def addNathan():
  global nathan,nathanNiceCounterFile
  nathanNiceCounterFile.seek(0)
  oldNathan = nathanNiceCounterFile.read().strip()
  newNathan = int(float(oldNathan))
  newNathan = newNathan + 1
  nathanNiceCounterFile.truncate(0)
  nathanNiceCounterFile.seek(0)
  nathanNiceCounterFile.write(str(newNathan))
  update()

def addJack():
  global jack,jackNiceCounterFile
  jackNiceCounterFile.seek(0)
  oldJack = jackNiceCounterFile.read().strip()
  newJack = int(float(oldJack))
  newJack = newJack + 1
  jackNiceCounterFile.truncate(0)
  jackNiceCounterFile.seek(0)
  jackNiceCounterFile.write(str(newJack))
  update()



@client.event
async def on_ready():
	print('Logged on as {0.user}'.format(client))


@client.event
async def on_message(message):
  content = message.content.lower()


  #censors your mom haha no free speech >:)
  #if re.compile('.*\\bm+o+m+\\b.*').match(content) != None:
   # await message.channel.purge(limit=1)
    #await message.channel.send('>:(')

  #if re.compile('.*\\bm+o+t+h+e+r+\\b.*').match(content) != None:
   # await message.channel.purge(limit=1)
    #await message.channel.send('>:(')

  #if re.compile('.*\\bm+a+m+a+\\b.*').match(content) != None:
   # await message.channel.purge(limit=1)
    #await message.channel.send('>:(')

  #if re.compile('.*\\bm+u+m+\\b.*').match(content) != None:
   # await message.channel.purge(limit=1)
    #await message.channel.send('>:(')

  #if re.compile('.*\\bm+o+m+m+a+\\b.*').match(content) != None:
   # await message.channel.purge(limit=1)
    #await message.channel.send('>:(')


  #send MMS and SMS ONLY WITH TWILIO VERIFIED PHONE NUMBERS BC IM BROKE AND IM NOT GOING TO BUY
  #TWILIO PREMIUM
  if message.content.startswith(':SMS'):
    args=content.split("/")
    twilioClient.api.account.messages.create(
      to="+1" + args[1],
      from_="+14159656430",
      body=args[2])
    
    await message.channel.send('Qiqi has delivered the message!')


    


  #nice counter
  if re.compile('.*\\bn+i+c+e+\\b.*').match(content) != None:
    if message.author.id == 700815706991755286:
      addVictor()
    if message.author.id == 333015213479821322:
      addJack()
    if message.author.id == 384361248533250051:
      addRoger()
    if message.author.id == 559835268014800896:
      addNathan()

  #prints a counter
  if message.content.startswith(':NiceCounter'):
    global roger, nathan, victor, jack
    await message.channel.send(
		    'Jack has said "nice" a total of ' + str(jack) +
		    ' times! \nNathan has said "nice" a total of ' +
		    str(nathan) +
		    ' times! \nVictor has said "nice" a total of ' +
		    str(victor) +
		    ' times! \nRoger has said "nice" a total of ' +
		    str(roger) + ' times!')

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

	#to email people
  if message.content.startswith(':email'):
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
      s.login(user=sender, password=os.getenv('GMAILPASS'))
      s.sendmail(sender, receiver, msg.as_string())
      s.quit()
      if temp == True:
        await message.channel.send('okay! qiqi will deliver the message')
    temp = True

	#spam email
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

	#tbh no idea what this is for
  if message.author == client.user:
    return

	#qiqi says hello
  if message.content.startswith(':hello'):
    await message.channel.send('I am Qiqi. I am a zombie. I forgot what comes next.')

	#qiqi says a voiceline
  if message.content.startswith(':qiqi'):
    out = QiqiLines[random.randint(0, len(QiqiLines) - 1)]
    await message.channel.send(out)

	#qiqi makes a ur mom joke!
  #if re.compile('.*\\bn+i+c+e+\\b.*').match(content) != None:
  #  await message.channel.send('ur MOM is nice Ha!')

	#qiqi wonders if ganyu is here
  if ('ganyu') in content:
    await message.channel.send('Did someone say Ganyu? Is Ganyu here? Qiqi would like some cocomilk please!')

	#qiqi returns a help
  if message.content.startswith(':help'):
    helpMessage = (":help - qiqi will help! \n:hello - says hi to me, Qiqi! \n:qiqi - qiqi will say something cool \n:email - :email/receiver's email/subject/message/qiqi 1 or qiqi 2 \nganyu - is cocogoat here? ")
    await message.channel.send(helpMessage)


keepAlive()
client.run(os.getenv('TOKEN'))