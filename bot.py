import discord
import os
import requests
import json
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from db import dBset
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='$')
keys = db.keys()


@client.event
async def on_ready():
    print('I am a stupid Python bot aka {0.user}'.format(client))


##LIST
@client.command(description='returns list of 100 coins')
async def list(ctx):
    cryptoList = [key for key in keys]
    await ctx.send(cryptoList)


##PRICE COIN
@client.command(description='$price <coin> to returns the current price of a coin')
async def price(ctx, id):
    if str(id).lower() in keys:
        await ctx.send(f'Current price of {id} is: {db[id]} USD')
    else:
        await ctx.send(
            f'{id} is not in the list, try visiting CoinGecko for reference')


# SEARCH COIN
@client.command(description='$search <keywords> to see coins with keywords related')
async def search(ctx, coin):
    id = str(coin).lower()
    cryptoList = [key for key in keys]
    msg = 'keywords you searched for: \n'
    for i in range(len(cryptoList)):
        if cryptoList[i].__contains__(id):
            msg += cryptoList[i] + '\n'
    await ctx.send(msg)


##MOTIVATION
@client.command(description='returns a quote')
async def motivation(ctx):
    u = 'https://zenquotes.io/api/random'
    r = requests.get(url=u)
    data = r.json()
    quote = data[0]['q'] + '-' + data[0]['a']
    await ctx.send(quote)


# OPGG
@client.command()
async def b(ctx, champ, lane, index):
    perk = [('Runes 1:', []), ('Runes 2:', []), ('Runes 3:', []),
            ('Runes 4:', [])]
    op_url = f'https://vn.op.gg/champion/{champ}/statistics/{lane}/build'
    data = requests.get(op_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    # r1
    r1 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-1"})
    wrap1 = r1[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes0 = wrap1[0].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes1 = wrap1[1].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes0_img = bigrunes0[0].find_all("img")
    bigrunes1_img = bigrunes1[0].find_all("img")
    perk[0][1].append('https:' + bigrunes0_img[0]['src'])
    perk[1][1].append('https:' + bigrunes1_img[0]['src'])

    smallrunes0 = wrap1[0].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    smallrunes1 = wrap1[1].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes0))
    for i in range(0, 5):
        smallrunes0_img = smallrunes0[i].find_all("img")
        smallrunes1_img = smallrunes1[i].find_all("img")
        perk[0][1].append('https:' + smallrunes0_img[0]['src'])
        perk[1][1].append('https:' + smallrunes1_img[0]['src'])
    #####################r2
    r2 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-2"})
    wrap2 = r2[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes2 = wrap2[0].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes3 = wrap2[1].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes2_img = bigrunes2[0].find_all("img")
    bigrunes3_img = bigrunes3[0].find_all("img")
    perk[2][1].append('https:' + bigrunes2_img[0]['src'])
    perk[3][1].append('https:' + bigrunes3_img[0]['src'])

    smallrunes2 = wrap2[0].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    smallrunes3 = wrap2[1].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes2))
    for i in range(0, 5):
        smallrunes2_img = smallrunes2[i].find_all("img")
        smallrunes3_img = smallrunes3[i].find_all("img")
        perk[2][1].append('https:' + smallrunes2_img[0]['src'])
        perk[3][1].append('https:' + smallrunes3_img[0]['src'])
    print(len(perk[int(index)][1]))

    fragmentpage = soup.find_all("div", {"class": "fragment-page"})
    shards = []
    for i in fragmentpage:
        p = i.find_all("div", {"class": "perk-page__image"})
        for j in p:
            shards.append(j.find_all("img", {"class": "active tip"}))
    url = []
    for i in shards:
        if i:
            for j in i:
                url.append('http:' + j['src'])
    for i in range(0, 3):
        perk[0][1].append(url[i])
    for i in range(3, 6):
        perk[1][1].append(url[i])
    for i in range(6, 9):
        perk[2][1].append(url[i])
    for i in range(9, 12):
        perk[3][1].append(url[i])
    for i in range(0, 9):
        await ctx.send(perk[int(index)][1][i])


@client.command(description='$c <champ> <lane> too see all runes on champion in embeded message')
async def c(ctx, champ, lane):
    perk = [('Runes 1:', []), ('Runes 2:', []), ('Runes 3:', []),
            ('Runes 4:', [])]
    op_url = f'https://vn.op.gg/champion/{champ}/statistics/{lane}/build'
    data = requests.get(op_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    # r1
    r1 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-1"})
    wrap1 = r1[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes0 = wrap1[0].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes1 = wrap1[1].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes0_img = bigrunes0[0].find_all("img")
    bigrunes1_img = bigrunes1[0].find_all("img")
    perk[0][1].append(bigrunes0_img[0]['alt'])
    perk[1][1].append(bigrunes1_img[0]['alt'])

    smallrunes0 = wrap1[0].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    smallrunes1 = wrap1[1].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes0))
    for i in range(0, 5):
        smallrunes0_img = smallrunes0[i].find_all("img")
        smallrunes1_img = smallrunes1[i].find_all("img")
        perk[0][1].append(smallrunes0_img[0]['alt'])
        perk[1][1].append(smallrunes1_img[0]['alt'])
    #####################r2
    r2 = soup.find_all("tbody", {"class": "tabItem ChampionKeystoneRune-2"})
    wrap2 = r2[0].find_all("div", {"class": "perk-page-wrap"})
    bigrunes2 = wrap2[0].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes3 = wrap2[1].find_all(
        "div", {
            "class":
                "perk-page__item perk-page__item--keystone perk-page__item--active"
        })
    bigrunes2_img = bigrunes2[0].find_all("img")
    bigrunes3_img = bigrunes3[0].find_all("img")
    perk[2][1].append(bigrunes2_img[0]['alt'])
    perk[3][1].append(bigrunes3_img[0]['alt'])

    smallrunes2 = wrap2[0].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    smallrunes3 = wrap2[1].find_all(
        "div", {"class": "perk-page__item perk-page__item--active"})
    print(len(smallrunes2))
    for i in range(0, 5):
        smallrunes2_img = smallrunes2[i].find_all("img")
        smallrunes3_img = smallrunes3[i].find_all("img")
        perk[2][1].append(smallrunes2_img[0]['alt'])
        perk[3][1].append(smallrunes3_img[0]['alt'])
    hero = soup.find_all("div", {"class": "champion-stats-header-info__image"})
    hero_img = hero[0].find_all("img")
    hero_img_url = 'https:' + hero_img[0]['src']
    emb = discord.Embed(title=f'{str(champ).upper()} RUNES ON VNOPGG',
                        color=discord.Colour.green())
    emb.set_thumbnail(url=hero_img_url)
    emb.add_field(name='Build number 0:', value=perk[0][1], inline=True)
    emb.add_field(name='Build number 1:', value=perk[1][1], inline=False)
    emb.add_field(name='Build number 2:', value=perk[2][1], inline=False)
    emb.add_field(name='Build number 3:', value=perk[3][1], inline=True)
    emb.set_author(name=f'{str(champ).capitalize()}', icon_url=hero_img_url)
    await ctx.send(embed=emb)


def fetch_yt():
    yt = build('youtube', 'v3', developerKey=os.environ.get('api_key'))
    nextPageToken = None
    items = []
    while True:
        pl_request = yt.playlistItems().list(
            part='contentDetails',
            playlistId='PLagj4mpqUoMPxJ9f1tpxwtaHLGdm8Hrw-',
            maxResults=50,
            pageToken=nextPageToken)
        pl_response = pl_request.execute()
        vid_ids = []
        for vid in pl_response['items']:
            vid_ids.append(vid['contentDetails']['videoId'])
        vid_request = yt.videos().list(part="contentDetails,snippet",
                                       id=','.join(vid_ids))
        vid_response = vid_request.execute()
        for item in vid_response['items']:
            items.append(item)
        nextPageToken = pl_response.get('nextPageToken')
        if not nextPageToken:
            break
    return items


yt = fetch_yt()


@client.command(description='$dobby <champ> to see video on dobby channel about the champ')
async def dobby(ctx, champ):
    titles = []
    urls = []
    for item in yt:
        titles.append(item['snippet']['title'])
        urls.append('https://www.youtube.com/watch?v=' + item['id'])
    champ = str(champ).capitalize()
    msg = ''
    for i in range(len(titles)):
        if str(titles[i]).__contains__(champ):
            msg += titles[i] + ': ' + urls[i] + '\n'
    await ctx.send(msg)


@client.command(description='$dobby_list to see all availble videos')
async def dobby_list(ctx):
    titles = []
    for item in yt:
        titles.append(item['snippet']['title'])
    text = '\n'.join(titles)
    await ctx.send(text)


@client.command(description='$skill <champ> <lane> to return skill order')
async def skill(ctx, champ, lane):
    op_url = f'https://vn.op.gg/champion/{champ}/statistics/{lane}/build'
    data = requests.get(op_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    table = soup.find(
        "table", {
            "class":
                "champion-overview__table champion-overview__table--summonerspell"
        })
    td = table.find_all("td", {"class": "champion-overview__data"})
    ul = []
    for t in td:
        ul.append(t.find_all("ul", {"class": "champion-stats__list"}))
    li = []
    for u in ul:
        for i in u:
            li.append(
                i.find_all("li", {"class": "champion-stats__list__item tip"}))
    msg = ''
    for f in li[2]:
        z = f.find_all("img")
        s = f.find_all("span")
        msg += str(s[0])[6]
        for i in z:
            await ctx.send('https:' + i['src'])
    toS = ''
    for i in msg:
        toS += i + '->'
    await ctx.send(toS + 'NULL')


###HELP COMMANDS
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
async def dobby(ctx):
    em = discord.Embed(title='Dobby', description="to see tips and tricks video for that champion",
                       color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$dobby <champ>")
    await ctx.send(embed=em)


@help.command()
async def price(ctx):
    em = discord.Embed(title='Price', description="to see the price of chosen coin", color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$price <coin>")
    await ctx.send(embed=em)


@help.command()
async def list(ctx):
    em = discord.Embed(title='LIST OF 100 COINS', description="display list of 100 coins", color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$list")
    await ctx.send(embed=em)


@help.command()
async def motivation(ctx):
    em = discord.Embed(title='MOTIVATE', description="MOTIVATES YOU", color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$motivation")
    await ctx.send(embed=em)


@help.command()
async def b(ctx):
    em = discord.Embed(title='RUNES', description="DISPLAYING RUNES OF A CHAMP IN A LANE (1 of 4 builds)",
                       color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$b <champ> <lane> <number>")
    await ctx.send(embed=em)


@help.command()
async def c(ctx):
    em = discord.Embed(title='RUNES OVERVIEW', description="displaying an embed of builds", color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$c <champ> <lane>")
    await ctx.send(embed=em)


@help.command()
async def dobby_list(ctx):
    em = discord.Embed(title='TIPS AND TRICKS PLAYLIST', description="displaying playlist src",
                       color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$dobby_list")
    await ctx.send(embed=em)


@help.command()
async def search(ctx):
    em = discord.Embed(title='SEARCH IN 100 COINS', description="dsearch coins", color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$search <cnt>")
    await ctx.send(embed=em)


@help.command()
async def skill(ctx):
    em = discord.Embed(title='LEVEL ORDER', description="displaying level order of a champion",
                       color=discord.Colour.blue())
    em.add_field(name="**Syntax**", value="$skill <champ> <lane>")
    await ctx.send(embed=em)


keep_alive()
client.run(os.environ.get('TOKEN'))
