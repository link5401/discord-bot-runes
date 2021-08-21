import discord
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



keep_alive()
my_secret = os.environ.get("TOKEN")
client.run(my_secret)

