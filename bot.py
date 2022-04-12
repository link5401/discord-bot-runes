import discord
import os
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands
from bs4 import BeautifulSoup
from opScrapper import opScrapper


client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('I am a stupid Python bot aka {0.user}'.format(client))

##MOTIVATION
@client.command(description='returns a quote')
async def motivation(ctx):
    u = 'https://zenquotes.io/api/random'
    r = requests.get(url=u)
    data = r.json()
    quote = data[0]['q'] + '-' + data[0]['a']
    await ctx.send(quote)

#OPGG
# @client.command()
# async def b(ctx, champ, lane, index):
#     pass


@client.command(description='$runes <champ> <lane> too see all runes on champion in embeded message')
async def runes(ctx, champ):
   op = opScrapper(champ)
   runes = op.findRunes()
   for r in runes:
       await ctx.send(r)


@client.command(description='$skill <champ> <lane> to return skill order')
async def skill(ctx, champ):
    op = opScrapper(champ)
    skills = op.findSkills()
    for s in skills:
       await ctx.send(s)


client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help",
                       description=f"contact me by mentioning @LINK#9706")
    helptext = ''
    for command in client.commands:
        helptext += f"\{command}: {command.description}\n"
    em.add_field(name='Commands', value=helptext)
    await ctx.send(embed=em)


 
@help.command()
async def motivation(ctx):
  em = discord.Embed(title ='MOTIVATE', description = "MOTIVATES YOU", color = discord.Colour.blue())
  em.add_field(name ="**Syntax**", value = "$motivation")
  await ctx.send(embed=em)
# @help.command()
# async def b(ctx):
#   em = discord.Embed(title ='RUNES', description = "DISPLAYING RUNES OF A CHAMP IN A LANE (1 of 4 builds)", color = discord.Colour.blue())
#   em.add_field(name ="**Syntax**", value = "$b <champ> <lane> <number>")
#   await ctx.send(embed=em)

@help.command()
async def rune(ctx):
  em = discord.Embed(title ='RUNES OVERVIEW', description = "displaying an embed of builds", color = discord.Colour.blue())
  em.add_field(name ="**Syntax**", value = "$rune <champ> <lane>")
  await ctx.send(embed=em)

@help.command()
async def skill(ctx):
  em = discord.Embed(title ='LEVEL ORDER', description = "displaying level order of a champion", color = discord.Colour.blue())
  em.add_field(name ="**Syntax**", value = "$skill <champ> <lane>")
  await ctx.send(embed=em)

keep_alive()
client.run(os.environ.get('TOKEN'))
