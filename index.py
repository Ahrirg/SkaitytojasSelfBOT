import selfcord
import asyncio
import os
import sys
from selfcord.ext import commands

CHANNAL_ID = 728579098854817792
bot = commands.Bot(command_prefix=';;', self_bot=True)

@bot.event
async def on_ready():
    print('Logged in hopefully ok!')
    channel = bot.get_channel(CHANNAL_ID)
    await channel.send('Am i ready?')

@bot.command()
async def ping(ctx):
    print('radom')

dir = os.getcwd()

async def PrintToUser(message, user):
    try:
        f = open(dir + '/Users/' + user + '.txt', 'x')
        f.close()
    except:
        x = 1

    file = open(dir + '/Users/' + user + '.txt','a')
    file.write(message)
    file.close()

async def PrintToServer(message, serverid):
    stringserverid = str(serverid)
    try:
        f = open(dir + '/Servers/' + stringserverid + '.txt', 'x')
        f.close()
    except:
        x = 1

    file = open(dir + '/Servers/' + stringserverid + '.txt','a')
    file.write(message)
    file.close()

@bot.event
async def on_message(message):
    if(message.content != ''):
        try:
            AuthorName = message.author.name
            AuthorChannelName = message.channel.name
            AuthorChannelid = message.channel.id
            AuthorServerName = message.guild.name
            AuthorServerid = message.guild.id
            AuthorContent = message.content
            isBot = message.author.bot
        except:
            print(f'[ERRORRAS BUVO]')

        fulltext = f'[{AuthorName}]([{AuthorServerName}][{AuthorChannelName}]) {AuthorContent}'
        IntoPersonText = f'([{AuthorServerName}][{AuthorChannelName}]) {AuthorContent}\n'
        IntoServerText = f'[{AuthorName}]([{AuthorChannelName}]) {AuthorContent}\n'

        if(AuthorName != 'sofdrg' and isBot == False):
            await PrintToUser(IntoPersonText, AuthorName)
            await PrintToServer(IntoServerText, AuthorServerid)

            print(fulltext)
            sys.stdout.flush()

            channel = bot.get_channel(CHANNAL_ID)
            await channel.send(f'([{AuthorServerName}][{AuthorChannelName}])\n[{AuthorName}] {AuthorContent}')


bot.run('MTIwOTU1ODYzNDA5OTM4NDM4MA.GcgNnM.lIrYbv4yffK-w0i-ahmnxhMOllDImuw5JqwaVo')