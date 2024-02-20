import discum
import sys
import asyncio
import os

bot = discum.Client(token='MTIwOTU1ODYzNDA5OTM4NDM4MA.GbsIeE.2KoFrktvOm4X8N7P6efI3cDHDEs9FY_-9FyTo0', log=False) #paste into USERTOKEN!!! (how to get, go to some youtube video idk) !!!!!!!!! important !!!!!!!!!!1

print('veik?')
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
    IntoPersonText = f'([ServerId={AuthorServerName}][ChannelId={AuthorChannelName}]) {AuthorContent}\n'
    IntoServerText = f'[{AuthorName}]([ChannelId={AuthorChannelName}]) {AuthorContent}\n'

    await PrintToUser(IntoPersonText, AuthorName)
    await PrintToServer(IntoServerText, AuthorServerid)
    
    print(fulltext)
    sys.stdout.flush()

@bot.gateway.command
def on_message(resp):
    if resp.event.message:
        message = resp.parsed.auto()

        if(message['content'] != ''):
            asyncio.run(main(message))

        

bot.gateway.run(auto_reconnect=True)
