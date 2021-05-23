import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import re

client = commands.Bot(command_prefix='#', help_command=None)

status = cycle(['미완성 봇'])   # 번갈아 표시할 상메

@client.event
async def on_ready():
    change_status.start()
    print("봇 이름:", client.user.name, "봇 아이디:", client.user.id, "봇 버전:", discord.__version__)


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))
for filename in os.listdir('./cogs'):   # cogs 폴더에 있는 명령어를 하나 씩 읽어옴
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['token'])
