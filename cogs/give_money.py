import discord
from discord import DMChannel
from discord.ext import commands


class Give_Money(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cogs
    @commands.command()
    async def 돈수정(self, ctx, *, text):

        users_money_text = open("./file/money.txt", "r", encoding='utf-8').readline()
        users_money = users_money_text.split(",")

        if ctx.author.id == 777496131177414656:
            text_list = text.split(' ')

            user_info = [0, 0]
            index = 0

            for user_money in users_money:
                if text_list[0] in user_money:
                    user_info = [user_money.split(' ')[0], user_money.split(' ')[1]]
                    break
                index += 1

            user_info[1] = str(int(user_info[1]) + int(text_list[1]))

            users_money[index] = f"{user_info[0]} {user_info[1]}"

            save = open("./file/money.txt", "w", encoding="utf-8")

            if len(users_money) > 1:
                save.write(",".join(users_money))
            save.close()

            user = await self.client.fetch_user(int(text_list[0]))

            if int(text_list[1]) < 0:
                embed = discord.Embed(title="[ 개발자님께서 E-Coin을 회수하셨어요.. ]", description=f'`{text_list[1]}`',
                                      color=0x62c1cc)
                embed.set_footer(text=f'남은 E-Coin: {user_info[1]}')
                await DMChannel.send(user, embed=embed)

                embed = discord.Embed(title=f"[ 회수 완료 ]", description=f'{user} `{text_list[1]}`',
                                      color=0x62c1cc)
                embed.set_footer(text=f'남은 E-Coin: {user_info[1]}')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="[ 개발자님께서 E-Coin을 지급해주셨어요! ]", description=f'`+{text_list[1]}`',
                                      color=0x62c1cc)
                embed.set_footer(text=f'남은 E-Coin: {user_info[1]}')
                await DMChannel.send(user, embed=embed)


def setup(client):
    client.add_cog(Give_Money(client))
