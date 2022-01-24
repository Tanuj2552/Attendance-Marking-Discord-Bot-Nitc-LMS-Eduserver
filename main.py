import discord
import os
from discord.ext import commands
import asyncio
from keep_alive import keep_alive
import pytz
from selenium import webdriver
import time
from datetime import datetime

bot = commands.Bot(command_prefix='!')
client = discord.Client()

username = "username" #replace with your lms username
password = "password" #replace with your lms password

def get_time():
    tz_NY = pytz.timezone('Asia/Kolkata')
    datetime_NY = datetime.now(tz_NY)
    now = datetime_NY.strftime("%H:%M:%S - (%d/%m)")
    return now


def markit():
    driver = webdriver.Firefox()
    url = 'https://eduserver.nitc.ac.in/login/index.php'

    driver.get(url)

    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    
    element = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/section/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button')
    

    driver.execute_script("arguments[0].click();", element)

    print('cool')
    driver.implicitly_wait(10)
    time.sleep(3)
    try:
        driver.find_element_by_partial_link_text('Attendance').click()
    except:
        return False

    time.sleep(2)
    driver.implicitly_wait(5)
    driver.find_element_by_link_text('Go to activity').click()
    driver.implicitly_wait(5)

    a = 1
    b = 0
    
    
    t = 0
    while (a and t <= 25):
        print("value of t is: "+ str(t))
        list = driver.find_elements_by_link_text('Submit attendance')
        if (list != []):
            b = 1

        if (b):
            time.sleep(2)
            driver.find_element_by_link_text('Submit attendance').click()
            time.sleep(2)
            driver.implicitly_wait(2)
            driver.find_elements_by_class_name('statusdesc')[0].click()
            driver.find_element_by_name('submitbutton').click()
            time.sleep(2)
            a = 0
            driver.close()
            return True
        else:
            driver.implicitly_wait(1)
            driver.refresh()
            time.sleep(5)

        t += 5

    driver.close()
    return False


async def finder():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(os.environ['channelId']))
    k = 0
    while (True):
        try:
            state = markit()
        except:
            time.sleep(100)
            continue
        if (state):
            time_now = get_time()    
            await channel.send("attendance marked at " + time_now)
        else:
            time_now = get_time()
            await channel.send("looped for " + str(k) + " times" + " at " + time_now)
            k += 1
        time.sleep(10)
    await asyncio.sleep(10)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


print("start")
keep_alive()

bot.loop.create_task(finder())
bot.run(os.environ['token'])
