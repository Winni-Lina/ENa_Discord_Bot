# disbot
Luke-68 님과 제작중인 디스코드 봇 disbot입니다
`초대 링크: https://discord.com/api/oauth2/authorize?client_id=844981326218264607&permissions=0&scope=bot`

- 봇 제작 툴
    - Discord Developer Portal(봇 몸체(?) 제작 사이트)  (extensions에서 python 다운 받아둘 것!)
    - 하루쿠(호스팅 페이지) -> 깃허브(하루쿠와의 연동)
    - 비쥬얼 스튜디오(프로그래밍 툴)
    - 깃허브 데스크탑(깃허브 commit and push)
    - 파이참 (Python 설치 후(Path설정 필수), 설치 / Tester 프로그램)
   
   
## 봇 base 제작 (개인설정은 생략함)
(봇 몸체(?) 제작)
1. Discord Developer Portal(사이트)에서 새로운 `Application` 추가   
2. `Bot`카테고리에서 `Build-A-Bot`에 `Add Bot`클릭 후, `Token` 메모장에 메모   
3. `OAuth2`카테고리에서 `Oauth2 URL Generator`에 `Bot`체크 후, 아래 링크 메모 (봇 초대 링크)   
   
   
(봇 메모리 제작)   
1. 깃허브 새로운 `Repository` 제작    
    - 다른 사람이 봐도 되는 자료라면 `public` 아니라면 `private`   
   
   
(봇 기초 프로그래밍)   
1. 깃허브 데스크탑에서 `Repository`를 `file`메뉴에서 `Clne Repository`선택   
2. `Github.com`에서 사용할 `Repository`를 선택 후, 클론 제작   
3. 해당 `Repository`를 선택 후, `Changes` 클릭한 후, 오른쪽 화면에 있는 `Open in Visual Studio Code` 클릭   
4. 아래 파일 또는 폴더들 제작   (파일명 아래에 있는 박스칸은 파일의 내용)   
    - cogs (폴더)   
    - runtime.txt   
        ```
            python-3.8.8
        ```
    - requirements.txt   
        ```
            discord.py
            asyncio
        ```
    - Procfile   
        ```
            worker: python main.py
        ```
    - main.py   
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
5. 깃허브 데스크탑에서 위 파일들을 `Commit`, `Push`를 진행   
   
   
(24시간 구동(호스팅))   
1. 하루쿠 사이트에서 새로운 `app` 제작   
2. `app` 들어가서 `setting`에 `add buildpack` 클릭 후, `Python` 선택   
3. 그 위 `Reveal Config Vars`에서 `Key`에 `token`입력, `Value`에 `메모장에 메모한 token값`입력   
4. `Deploy`에 `Github Repository`연결 후, 맨 아래 `Manual deploy`에서 `Deploy Branch` 클릭   
5. `Deploy Branch` 클릭 후, 끝났다면, `Overveiw` 들어가서 `Dyno formation` 옆 `Configure Dyno` 클릭   
6. `Resources`에서 `worker`을 통해`봇 온오프 설정`(오른쪽 on/왼쪽 off)   
   
   
## 봇 Tester 세팅 (Pycharm)
1. 새로운 `Project` 생성 (이름은 Temp)) (인터프리터 따로 설정하기 위함)
2. 생성한 `Project` 로딩 끝나면, `File`에서 `Project close`
3. 기본 경로를 기준으로 파일탐색창에서 `C:\Users\(사용자이름)\Documents\GitHub`에 있는 자신의 봇 파일을 복사해 `C:\Users\(사용자이름)\PycharmProjects`에 붙여넣기
4. `Pycharm`에서 `Open File or Project` 복사한 파일 열기
5. `cog`폴더와 `main.py`를 제외한 모든 파일 제거
6. `main.py`에 마지막 `client.run('복사한 토큰값으로 수정')`
7. 하루쿠를 오프 후, `main.py`를 작동 시켰을 때, 봇이 `on`된다면, 테스트 파일 완성
















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
    client.add_cog(명령어영문이름(client))

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
        
