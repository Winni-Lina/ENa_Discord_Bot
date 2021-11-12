from discord.ext import commands


class Ena(commands.Cog):
    def __init__(self, client):
        self.client = client

    #cogs
    @commands.command()
    async def 이나야(self, ctx, *, text):
        developer = await self.client.fetch_user(777496131177414656)
        bot = await self.client.fetch_user(882995163427913738)

        text_list = text.split(" ")

        if text_list[0] == "심심해":
            await ctx.send("이나도 심심해요..ㅠ")

        elif text_list[0] == "개발자" or text_list[0] == "개발자는?":
            await ctx.send(f"`{developer}`님입니다!")

        elif text_list[0] == "일해":
            if ctx.author.id == 777496131177414656:
                await ctx.send("일해라 개발자! <@777496131177414656>")
            else:
                await ctx.send("보이진 않아도 열심히하고 있어요! 아마도요..?")


def setup(client):
    client.add_cog(Ena(client))