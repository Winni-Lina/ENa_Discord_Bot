import discord
import asyncio
 
client = discord.Client()
 
@client.event
async def on_ready(): 
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("서술"))
 
@client.event
async def on_message(message): 
    content = message.content 
    guild = message.guild 
    author = message.author 
    channel = message.channel 
    if content.startswith("!test"): 
        await message.channel.send("test" + message.content) 
    if content == "!ping": 
        await message.channel.send("Pong!") 
 
client.run('ODQ0OTgxMzI2MjE4MjY0NjA3.YKaULw.pc0Gb0QGYfp_4106lNBnlx-c_UU')