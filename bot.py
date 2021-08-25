import discord
import os
import random
import requests
import json
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from bs4 import BeautifulSoup
from datetime import datetime
client = commands.Bot(command_prefix='$')

@client.event
async def  on_ready():
    print('I am a stupid Python bot aka {0.user}'.format(client))
@client.command()
async def bot_master(ctx):
    github_icon = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png'
    img_url = 'https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.6435-9/134079334_1564269020627947_7628475970815779425_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=liBumNmxNLwAX9m5gfr&tn=DYlMl_xALjPkESeE&_nc_ht=scontent.fsgn2-3.fna&oh=e09d72c99c01a16af0a95bcb4d265bc7&oe=614B5C4A'
    facebok_icon = 'https://image.similarpng.com/very-thumbnail/2020/04/Popular-Logo-facebook-icon-png.png'
    emb = discord.Embed(title='La Duong Xuan Linh', description= 'Junior at HCMUT',color = discord.Colour.blue())
    emb.set_thumbnail(url=img_url)
    emb.set_author(name='Author info: ',icon_url=img_url)
    emb.add_field(name= 'My git hub:', value= 'https://github.com/link5401', inline=True)
    emb.add_field(name= 'My facebook: ', value= 'https://www.facebook.com/profile.php?id=100011345917376', inline=True)
    await ctx.send(embed=emb)

@client.command()
async def b(ctx,champ,lane,index):
    perk = [
        ('Runes 1:',[]),
        ('Runes 2:',[]),
        ('Runes 3:',[]),
        ('Runes 4:',[])
    ]
    op_url = f'https://vn.op.gg/champion/{champ}/statistics/{lane}/build'
    data = requests.get(op_url)
    soup = BeautifulSoup(data.text,'html.parser')
    #r1
    r1 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-1"})
    wrap1 = r1[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes0 = wrap1[0].find_all("div",{"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes1 = wrap1[1].find_all("div",{"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes0_img =bigrunes0[0].find_all("img")
    bigrunes1_img =bigrunes1[0].find_all("img")
    perk[0][1].append('https:' + bigrunes0_img[0]['src'])
    perk[1][1].append('https:' + bigrunes1_img[0]['src'])

    smallrunes0 = wrap1[0].find_all("div",{"class": "perk-page__item perk-page__item--active"})
    smallrunes1 = wrap1[1].find_all("div",{"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes0))
    for i in range(0,5):
        smallrunes0_img = smallrunes0[i].find_all("img")
        smallrunes1_img = smallrunes1[i].find_all("img")
        perk[0][1].append('https:' + smallrunes0_img[0]['src'])
        perk[1][1].append('https:' + smallrunes1_img[0]['src'])
    #####################r2
    r2 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-2"})
    wrap2 = r2[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes2 = wrap2[0].find_all("div", {"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes3 = wrap2[1].find_all("div", {"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes2_img = bigrunes2[0].find_all("img")
    bigrunes3_img = bigrunes3[0].find_all("img")
    perk[2][1].append('https:' + bigrunes2_img[0]['src'])
    perk[3][1].append('https:' + bigrunes3_img[0]['src'])

    smallrunes2 = wrap2[0].find_all("div", {"class": "perk-page__item perk-page__item--active"})
    smallrunes3 = wrap2[1].find_all("div", {"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes2))
    for i in range(0, 5):
        smallrunes2_img = smallrunes2[i].find_all("img")
        smallrunes3_img = smallrunes3[i].find_all("img")
        perk[2][1].append('https:' + smallrunes2_img[0]['src'])
        perk[3][1].append('https:' + smallrunes3_img[0]['src'])
    print(len(perk[int(index)][1]))
    for i in range(0, 6):
        await ctx.send(perk[int(index)][1][i])
@client.command()
async def c(ctx,champ,lane):
    perk = [
        ('Runes 1:',[]),
        ('Runes 2:',[]),
        ('Runes 3:',[]),
        ('Runes 4:',[])
    ]
    op_url = f'https://vn.op.gg/champion/{champ}/statistics/{lane}/build'
    data = requests.get(op_url)
    soup = BeautifulSoup(data.text,'html.parser')
    #r1
    r1 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-1"})
    wrap1 = r1[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes0 = wrap1[0].find_all("div",{"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes1 = wrap1[1].find_all("div",{"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes0_img =bigrunes0[0].find_all("img")
    bigrunes1_img =bigrunes1[0].find_all("img")
    perk[0][1].append(bigrunes0_img[0]['alt'])
    perk[1][1].append(bigrunes1_img[0]['alt'])

    smallrunes0 = wrap1[0].find_all("div",{"class": "perk-page__item perk-page__item--active"})
    smallrunes1 = wrap1[1].find_all("div",{"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes0))
    for i in range(0,5):
        smallrunes0_img = smallrunes0[i].find_all("img")
        smallrunes1_img = smallrunes1[i].find_all("img")
        perk[0][1].append(smallrunes0_img[0]['alt'])
        perk[1][1].append(smallrunes1_img[0]['alt'])
    #####################r2
    r2 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-2"})
    wrap2 = r2[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes2 = wrap2[0].find_all("div", {"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes3 = wrap2[1].find_all("div", {"class": "perk-page__item perk-page__item--keystone perk-page__item--active"})
    bigrunes2_img = bigrunes2[0].find_all("img")
    bigrunes3_img = bigrunes3[0].find_all("img")
    perk[2][1].append(bigrunes2_img[0]['alt'])
    perk[3][1].append(bigrunes3_img[0]['alt'])

    smallrunes2 = wrap2[0].find_all("div", {"class": "perk-page__item perk-page__item--active"})
    smallrunes3 = wrap2[1].find_all("div", {"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes2))
    for i in range(0, 5):
        smallrunes2_img = smallrunes2[i].find_all("img")
        smallrunes3_img = smallrunes3[i].find_all("img")
        perk[2][1].append(smallrunes2_img[0]['alt'])
        perk[3][1].append(smallrunes3_img[0]['alt'])
    hero = soup.find_all("div",{"class": "champion-stats-header-info__image"})
    hero_img = hero[0].find_all("img")
    hero_img_url = 'https:' + hero_img[0]['src']
    emb = discord.Embed(title=f'{str(champ).upper()} RUNES ON VNOPGG',color=discord.Colour.green())
    emb.set_thumbnail(url=hero_img_url)
    emb.add_field(name='Build number 0:', value= perk[0][1],inline= True)
    emb.add_field(name='Build number 1:', value= perk[1][1],inline= False)
    emb.add_field(name='Build number 2:', value= perk[2][1],inline= False)
    emb.add_field(name='Build number 3:', value= perk[3][1],inline= True)
    emb.set_author(name=f'{str(champ).capitalize()}',icon_url=hero_img_url)
    await ctx.send(embed=emb)


keep_alive()
client.run(os.environ.get('TOKEN'))
