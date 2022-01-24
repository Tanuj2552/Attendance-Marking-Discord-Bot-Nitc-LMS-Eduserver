# NITC-LMS-Attendance-Marking-Discord-Bot
This bot is used for marking attendance links as "present" for possibly every class. This only works for NIT Calicut Eduserver LMS.


The automation of the bot is achieved by using discord.py (https://discordpy.readthedocs.io/en/stable/#)


The hosting/implementation of the bot is done in Replit (https://replit.com/~)

# Steps
1) First create a python repl in replit platform and upload the given py codes (main and keep_alive) in this repository into that repl, and replace the username and password in the code with your username and password of NITC LMS Eduserver.
2) Install the gecko_driver (https://askubuntu.com/a/871077) (via shell in repl) for automating the mozilla firefox browser, which is pre-installed in the repl.
3) Create a discord bot (https://www.freecodecamp.org/news/create-a-discord-bot-with-python/). Do not copy the code from this blog. Only follow the process of creating bot and make note of the token of the bot and channelId of the discord channel and add them to the secret environment variables in the repl with apt key-value names and values (lock symbol in the left side bar)
4) Run the bot and watch it marking your attendance.

# Note 
This bot only sometimes helps in marking your attendance (when you forgot about the class or slept through it xD), but may not be able to mark attendance of every class because the lms is usually very slow at some times of the day resulting in its failure sometimes. It has helped me a couple of times (atleast 2-3 classes per day).

Sometimes the bot may stop running (bcoz of various reasons (server down, lms speed, etc)). So open the replit site if you feel the bot is not running and restart it.

Please dont blame the bot if you miss any attendance, as I said it helps you sometimes but you cannot rely on it completely for marking attendance.
