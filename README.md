# Qiqi Bot
A Discord bot that uses Python to complete simple tasks such as altering messages and sending emails.

#Features
>help - returns a list of commands
>hello - qiqi introduces herself
>qiqi - returns a random voiceline
>email/receiver's email/subject/body/1 or 2
>spamemail/receiver's email/number of emails/body/1 or 2
>r34 - gets a random image from rule34 if not passed a parameter, gets a random image from rule34 with a specific tag if passed 1 parameter
>ls or >lightshot - returns a random screenshot from lightshot
>reddit - returns a random post from r/memes if no parameters are passed, gets a ramdom image from r/*parameter* if 1 parameter is passed

# Notes

autoQiqi.bat and launch_bat.vbs is an a way for qiqiBot to go online automatically on computer startup.
autoQiqi.bat runs the bot.py python file through a command line when called.
launch_bat.vbs makes the command prompt screen invisible after the batch file puts qiqiBot online

The *1 or 2* in the last parameter of the email commands is just to choose which email to send the emails from. I have two emails created for this bot, and 1 or 2 just chooses between them.

All python files needed to run the bot are located in the Files folder
- bot.py contains everything that is needed to interact with discord
- keepAlive.py is needed if qiqiBot is being hosted on replit. It pings the bot before it shuts down
- rule34.py is needed for the r34 command to work properly. It scrapes the rule34 website for specific or random images.
- sendmail.py is needed for sending emails.
- test.py is my own personal test file. You may ignore this file
- voicelines.py returns a random voiceline from the character Qiqi from the game, Genshin Impact
