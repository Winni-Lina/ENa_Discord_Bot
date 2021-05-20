import os
import discord


import discord
import os
from discord import client
from discord.enums import Status
from discord.ext import commands, tasks
from itertools import cycle
import re

client = commands.Bot(command_prefix='#', help_command=None)

Status = cycle(['NACL', 'Shio'])

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(Status=discord.Status.online,activity=discord.Game(next(status)))

for filename in os.listdir ('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

client.run(os.environ['token'])