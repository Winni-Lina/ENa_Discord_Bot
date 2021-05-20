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

#@tasks.loop(seconds=10)

client.run(os.environ['token'])