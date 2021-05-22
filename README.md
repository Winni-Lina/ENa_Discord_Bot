# discordbot
Luke-68 님과 제작중인 디스코드 봇 disbot입니다

`초대 링크: https://discord.com/api/oauth2/authorize?client_id=844981326218264607&permissions=0&scope=bot`
##  main.py 메모
```python
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='#', help_command=None)

status = cycle(['미완성 봇'])  # 번갈아 표시할 상메


@client.event
async def on_ready():
    change_status.start()
    print("봇 이름:", client.user.name, "봇 아이디:", client.user.id, "봇 버전:", discord.__version__)


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))


for filename in os.listdir('./cogs'):  # cogs 폴더에 있는 명령어를 하나 씩 읽어옴
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['token'])

```
- 상태 메세지 표시    
`#activity=discord.Game(name="내용")                   # ~ 하는 중`      
`#activity=discord.Streaming(name="내용", url="링크")   # ~ 방송 중`    
`#activity=discord.Activity(type=discord.ActivityType.listening, name="내용")  # ~ 듣는 중`       
`#activity=discord.Game(next(status))  #위 status에 선언된 리스트의 값들이 번갈아가며 표시됨`

## cogs파일 안 명령어 기본 코드
```python
import discord
from discord.ext import commands


class 명령어영문이름(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cogs
    @commands.command()
    async def 명령어이름(self, ctx):
        # 명령어 내용 입력
        

def setup(client):
    client.add_cog(명령(client))

```
`한국어로 된 부분은 수정해야되는 부분 (다른 명령어와 중복 X)`   
`명령어 내용 입력 주석 아래에 임베드 또는 일반 메세지를 사용해 명령어 후 내용을 작성하면 된다.`  
```python
#메세지 사용 방법
    @commands.command()
    async def 명령어이름(self, ctx):
       # 명령어 내용 입력
        await ctx.send("내용 입력")
```
```python
#임베드 사용 방법      자료 참고:https://nashio.tistory.com/3?category=877811
    @commands.command()
    async def 명령어이름(self, ctx):
       # 명령어 내용 입력
        await ctx.trigger_typing()
        embed = discord.Embed(title="알맞는 내용 입력")
        await ctx.send(embed=embed)

```
        
