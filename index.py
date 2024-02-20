import discum
import sys
import json
import asyncio
import os
bot = discum.Client(token='MTIwOTU1ODYzNDA5OTM4NDM4MA.GBNJXi._jX1jtXDUixPXhr2HTw1QropKBMILDc0Xw4CXw', log=False)

bot.sendMessage("728579098854817792", "Turning online :3")

dir = os.getcwd()

@bot.gateway.command
def on_ready(resp):
  if resp.event.ready_supplemental: #ready_supplemental is sent onready
    user = bot.gateway.session.user # parsing the current user
    username = user['username']
    yourself = f"{username}"
    print(f"ready and logged in as {yourself}")



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

async def main(message):
    try:
        AuthorName = message['author']['username']
        AuthorChannelName = message['channel_id']
        AuthorChannelid = message['channel_id']
        AuthorServerName = message['guild_id']
        AuthorServerid = message['guild_id']
        AuthorContent = message['content']
    except:
        print(f'[ERRORRAS BUVO]')

    fulltext = f'[{AuthorName}]([{AuthorServerName}][{AuthorChannelName}]) {AuthorContent}'
    IntoPersonText = f'([ServerName={AuthorServerName}][ChannelName={AuthorChannelName}]) {AuthorContent}\n'
    IntoServerText = f'[{AuthorName}]([ChannelName={AuthorChannelName}]) {AuthorContent}\n'

    await PrintToUser(IntoPersonText, AuthorName)
    await PrintToServer(IntoServerText, AuthorServerid)
    
    print(fulltext)
    sys.stdout.flush()

@bot.gateway.command
def on_message(resp):
    if resp.event.message:
        message = resp.parsed.auto()

        asyncio.run(main(message))

        

bot.gateway.run(auto_reconnect=True)
