# Qiqi Bot
A Discord bot that uses Python to complete simple tasks such as altering messages and sending emails.

# Features (Commands) with prefix '>'

help - returns a list of commands

hello - qiqi introduces herself

qiqi - returns a random voiceline

email/receiver's email/subject/body/1 or 2

spamemail/receiver's email/number of emails/body/1 or 2

ls or lightshot - returns a random screenshot from lightshot

reddit - returns a random post from r/memes if no parameters are passed, gets a ramdom image from r/*parameter* if 1 parameter is passed

pfp - returns the avatar picture of whoever is mentioned

# Notes

autoQiqi.bat and launch_bat.vbs is an a way for qiqiBot to go online automatically on computer startup.
autoQiqi.bat runs the bot.py python file through a command line when called.
launch_bat.vbs makes the command prompt screen invisible after the batch file puts qiqiBot online

The *1 or 2* in the last parameter of the email commands is just to choose which email to send the emails from. I have two emails created for this bot, and 1 or 2 just chooses between them.

All python files needed to run the bot are located in the Files folder
- bot.py contains everything that is needed to interact with discord
- keepAlive.py is needed if qiqiBot is being hosted on replit. It pings the bot before it shuts down
- sendmail.py is needed for sending emails.
- test.py is my own personal test file. You may ignore this file
- voicelines.py returns a random voiceline from the character Qiqi from the game, Genshin Impact
