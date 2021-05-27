# Qiqi Bot
A Discord bot that uses Python to complete simple tasks such as altering messages and sending emails.

# Notes

autoQiqi.bat and launch_bat.vbs is an a way for qiqiBot to go online automatically on computer startup.
autoQiqi.bat runs the bot.py python file through a command line when called
launch_bat.vbs makes the command prompt screen invisible after the batch file puts qiqiBot online

All python files needed to run the bot are located in the Files folder
- bot.py contains everything that is needed to interact with discord
- keepAlive.py is needed if qiqiBot is being hosted on replit. It pings the bot before it shuts down
- rule34.py is needed for the r34 command to work properly. It scrapes the rule34 website for specific or random images.
- sendmail.py is needed for sending emails.
- test.py is my own personal test file. You may ignore this file
- voicelines.py returns a random voiceline from the character Qiqi from the game, Genshin Impact
