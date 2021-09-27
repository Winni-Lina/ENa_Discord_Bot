import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import re

token = open("token", "r").readline()
client = commands.Bot(command_prefix='~e', help_command=None)

status = cycle(['E.Na 봇 작동중', '테스트 중입니다.'])

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)

