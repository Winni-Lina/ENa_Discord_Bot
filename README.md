# discordbot
Luke-68 님과 제작중인 디스코드 봇 disbot입니다

`초대 링크: https://discord.com/api/oauth2/authorize?client_id=844981326218264607&permissions=0&scope=bot`
##  main.py 메모
```python
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import re

client = commands.Bot(command_prefix='#', help_command=None)

status = cycle(['미완성 봇']) #번갈아 표시할 상메

@client.event
async def on_ready():
    change_status.start()
    print("봇 이름:", client.user.name, "봇 아이디:", client.user.id, "봇 버전:", discord.__version__)


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))

for filename in os.listdir('./commands'):   #commands 폴더에 있는 명령어를 하나 씩 읽어옴
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['token'])
```

`#activity=discord.Game(name="내용")                   # ~ 하는 중`
`#activity=discord.Streaming(name="내용", url="링크")   # ~ 방송 중`
`#activity=discord.Activity(type=discord.ActivityType.listening, name="내용")  # ~ 듣는 중`
`#activity=discord.Game(next(status))  #위 status에 선언된 리스트의 값들이 번갈아가며 표시됨`
