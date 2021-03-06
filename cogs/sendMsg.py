import discord
from discord.ext import commands
from discord import DMChannel
import time

class sendMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 전송(self, ctx, *, text):
        developer = await self.client.fetch_user(777496131177414656)
        bot = await self.client.fetch_user(882995163427913738)

        ignoreUser = open("./file/ignoreUser.txt", "r", encoding='utf-8').readline()
        ignore_ids = ignoreUser.split(",")

        now = time.localtime()
        if ctx.author.id == 777496131177414656:
            textlist = text.split(" ")
            text = " ".join(textlist[1:])
            embed = discord.Embed(title="[ 메세지가 도착했습니다 ]", description=f"```{text}```", color=0x62c1cc)
            embed.set_author(name=f'E.Na Developer: {developer}')
            embed.set_thumbnail(url=developer.avatar_url)
            embed.add_field(name="**답장하기**", value="`~전송` (내용)")
            embed.set_footer(text="%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
            user = await self.client.fetch_user(int(textlist[0]))
            await DMChannel.send(user, embed=embed)
            await ctx.send(f"전송 완료했습니다. / 유저: {user.name} / 메세지: {text}")
        else:
            if str(ctx.author.id) in ignore_ids:
                await ctx.send('차단되어있습니다.')
            else:
                mygu = self.client.get_guild(894257659237236776)
                botch = mygu.get_channel(894268416196767764)

                embed = discord.Embed(title="[ 메세지가 도착했습니다 ]", description=f"```{text}```", color=0x62c1cc)
                embed.set_author(name=f"{ctx.author.name}")
                embed.add_field(name="유저 id", value=ctx.author.id)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text="%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
                await botch.send(embed=embed)

                embed = discord.Embed(title="[ 성공적으로 메세지가 전송되었습니다 ]", description='불쾌감을 주는 메세지인 경우, 차단의 대상이 되실 수 있습니다.',color=0x62c1cc)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(sendMsg(client))