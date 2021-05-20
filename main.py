import discord
from discord.ext import commands
import os

app = commands.Bot(command_prefix = '-')

@app.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await app.change_presence(status=discord.Status.online)

  await app.change_presence(activity=discord.Game(name="게임"))
  #await app.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await app.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await app.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",app.user.name,"봇 아이디:",app.user.id,"봇 버전:",discord.__version__)


app.run(os.environ['token'])