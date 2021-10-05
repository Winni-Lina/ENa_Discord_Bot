import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

token = open("./ignore/token.txt", "r").readline()
client = commands.Bot(command_prefix='~', help_command=None)

status = cycle(['E.Na 봇 작동', '정상 작동'])

@client.event
async def on_ready():
    change_status.start()
    print("이나 봇 작동 시작합니다.")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['token'])

