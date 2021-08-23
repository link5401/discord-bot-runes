import discord
import gunicorn
import os
import requests
import json
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import time
from multiprocessing.pool import ThreadPool
import urllib.request
import re
import io
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ffmpeg
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
client = commands.Bot(command_prefix='$')
@client.event
async def  on_ready():
    print('I am a stupid Python bot aka {0.user}'.format(client))


#help
client.remove_command('help')
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title= "Help", description="Use $help <command> for instructions")
    em.add_field(name='commands:',value='$runes\n$items\n$levels\n$runes,$items and $levels commands are only availale when im online because server nhu cac')
    await ctx.send(embed=em)
@help.command()
async def runes(ctx):
    em = discord.Embed(titled = "Runes", description= "Gets yo runes")
    em.add_field(name = "**Syntax**", value = "$runes <champ> <lane>")
    await ctx.send(embed = em)
@help.command()
async def items(ctx):
    em = discord.Embed(titled = "Items", description= "Gets yo items")
    em.add_field(name = "**Syntax**", value = "$items <champ> <lane>")
    await ctx.send(embed = em)
@help.command()
async def levels(ctx):
    em = discord.Embed(titled = "Levels", description= "Gets yo levels")
    em.add_field(name = "**Syntax**", value = "$levels <champ> <lane>")
    await ctx.send(embed = em)


@client.command()
async def runes(ctx, champ, lane):
    async with ctx.typing():
        print('ran into cmd')
        google_chrome_options = webdriver.ChromeOptions()
        google_chrome_options.add_argument('--disable-gpu')
        google_chrome_options.add_argument('--no-sandbox')
        google_chrome_options.binary_location = GOOGLE_CHROME_PATH
        google_chrome_options.headless = True
        google_chrome_options.add_argument('--window-size=1920,3000')
        web_driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            options=google_chrome_options
        )
        url = f"https://op.gg/champion/{champ}/statistics/{lane}"
        await ctx.send("Build :\n")
    async with ctx.typing():
        web_driver.get(url)
        web_driver.save_screenshot("element.png")
        im = Image.open('element.png')
        im = im.crop((420, 1860, 1150, 2460))
        web_driver.close()
        im.save('runes1.png')
        await ctx.send(
            file=discord.File("runes1.png")
        )

@client.command()
async def levels(ctx, champ, lane):
    async with ctx.typing():
        print('ran into cmd')
        google_chrome_options = webdriver.ChromeOptions()
        google_chrome_options.add_argument('--disable-gpu')
        google_chrome_options.add_argument('--no-sandbox')
        google_chrome_options.headless = True
        google_chrome_options.add_argument('--window-size=1920,3000')
        web_driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            options=google_chrome_options
        )
        url = f"https://op.gg/champion/{champ}/statistics/{lane}"
        await ctx.send("Levels :\n")
    async with ctx.typing():
        web_driver.get(url)
        web_driver.save_screenshot("element.png")
        im = Image.open('element.png')
        im = im.crop((420, 1000, 1150, 1170))
        web_driver.close()
        im.save('skills1.png')
        await ctx.send(
            file=discord.File("skills1.png")
        )

@client.command()
async def items(ctx, champ, lane):
    async with ctx.typing():
        print('ran into cmd')
        google_chrome_options = webdriver.ChromeOptions()
        google_chrome_options.add_argument('--disable-gpu')
        google_chrome_options.add_argument('--no-sandbox')
        google_chrome_options.add_argument('--disable-dev-shm-usage')
        google_chrome_options.headless = True
        google_chrome_options.add_argument('--window-size=1920,3000')
        web_driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            options=google_chrome_options
        )
        url = f"https://op.gg/champion/{champ}/statistics/{lane}"
        await ctx.send("Items :\n")
    async with ctx.typing():
        web_driver.get(url)
        web_driver.save_screenshot("element.png")
        im = Image.open('element.png')
        im = im.crop((420, 1185, 1150, 1850))
        web_driver.close()
        im.save('items1.png')
        await ctx.send(
            file=discord.File("items1.png")
        )
@client.command()
async def test(ctx):
    ctx.send("Bot oc cho")
keep_alive()
my_secret = os.environ.get("TOKEN")
client.run(my_secret)

