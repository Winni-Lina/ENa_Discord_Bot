import random

import discord
from discord.ext import commands


class Gambling(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cogs
    @commands.command()
    async def 도박(self, ctx, *, text):
        users_money_text = open("./file/money.txt", "r", encoding='utf-8').readline()
        users_money = users_money_text.split(",")

        random_num = random.sample([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5],1)
        user_info = [0, 0]
        text_list = text.split(' ')
        index = 0
        gambling_coin = int(text_list[0])

        for user_money in users_money:
            if str(ctx.author.id) in user_money:
                user_info = [user_money.split(' ')[0], user_money.split(' ')[1]]
                print(user_info)
                break
            index += 1

        if int(user_info[1]) >= gambling_coin:
            if random_num[0] == 0:
                users_money[index] = f"{user_info[0]} {str(int(user_info[1]) - gambling_coin)}"
                embed = discord.Embed(title=f"[ E-Coin을 잃었습니다 ]",
                                      description=f'`-{gambling_coin}`', color=0x62c1cc)
                embed.set_footer(text=f"남은 E-Coin: {int(user_info[1]) - gambling_coin}")
                await ctx.send(embed=embed)
            else:
                users_money[index] = f'{user_info[0]} {int(user_info[1]) + gambling_coin * random_num[0]}'
                embed = discord.Embed(title=f"[ 축하합니다! {random_num[0]}배에 성공하셨습니다! ]",
                                      description=f'`+{gambling_coin * random_num[0]}`', color=0x62c1cc)
                embed.set_footer(text=f"총 보유 E-Coin: {int(user_info[1]) + gambling_coin * random_num[0]}")
                await ctx.send(embed=embed)


            save = open("./file/money.txt", "w", encoding="utf-8")
            if len(users_money) > 1:
                save.write(",".join(users_money))
            save.close()


        else:
            embed = discord.Embed(title="[ E-Coin이 없습니다 ]", description='`~돈줘`를 입력해 돈을 받으세요!', color=0x62c1cc)
            await ctx.send(embed=embed)
            return


def setup(client):
    client.add_cog(Gambling(client))
