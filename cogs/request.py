import discord
from discord.ext import commands
import time

class request(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ignore_id = []

    #cogs
    @commands.command()
    async def 요청(self, ctx, *, text):
        if ctx.author.id in self.ignore_id:
            await ctx.send('요청이 차단되어있습니다.')
        else:
            now = time.localtime()
            mygu = self.client.get_guild(790535644883320842)
            botch = mygu.get_channel(892019559807209473)

            embed1 = discord.Embed(title='[ 새로운 요청이 도착했습니다 ]', description=f'요청자: {ctx.author}\n서버 id: {ctx.guild.id}\n요청자 id: {ctx.author.id}', color=0x62c1cc)
            embed1.add_field(name='요청 내용', value=text, inline=True)
            embed1.set_thumbnail(url=ctx.author.avatar_url)
            embed1.set_footer(text="%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
            await botch.send(f"<@777496131177414656>")
            await botch.send(embed=embed1)

            embed2 = discord.Embed(title='[ 성공적으로 요청이 전송됐습니다 ]', description=f"요청 내용: {text}", color=0x62c1cc)
            embed2.add_field(name="**요청해주셔서 감사합니다!**", value="구현이 되는 대로 알려드리겠습니다!")
            embed2.set_thumbnail(url='https://cdn.discordapp.com/attachments/891875793783902218/891875843826135040/29841_R8odfZL3.png')
            embed2.set_footer(text='이상한 요청을 할 경우, 요청 차단이 될 수 있습니다.',icon_url='https://cdn.discordapp.com/avatars/777496131177414656/eedb299fd8b1860a80b15a5c0c5d5168.webp?size=1024')
            await ctx.send(embed=embed2)

def setup(client):
    client.add_cog(request(client))