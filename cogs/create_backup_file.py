import discord
from discord.ext import commands
import os
import time

class Backup_file(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cogs
    @commands.command()
    async def 백업저장(self, ctx):
        if ctx.author.id == 777496131177414656:
            gu = self.client.get_guild(894257659237236776)
            ch = gu.get_channel(912921395275649054)
            now = time.localtime()
            embed = discord.Embed(title="백업파일 저장이 완료되었습니다", description="")
            await ctx.send(embed=embed)
            await ch.send("```ini\n[ 백업파일 %04d/%02d/%02d %02d:%02d:%02d 본]```"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
            await ch.send(file=discord.File(r'./file/money.txt'))
            await ch.send(file=discord.File(r'./file/ignoreUser.txt'))


def setup(client):
    client.add_cog(Backup_file(client))
