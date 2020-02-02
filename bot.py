# bot.py
import discord
import local_settings
import random as r
import re


def roll(i, l):
    rolls = []
    for k in range(0, l[0]):
        rolls.append(r.randint(1, l[1]))
    if i == 1:
        rolls.append(sum(rolls) + l[2])
    elif i == 2:
        rolls.append(sum(rolls) - l[2])
    else:
        rolls.append(sum(rolls))
    return rolls


def basic_roll(l):
    return int(r.randint(1, l[0]))


if __name__ == '__main__':

    TOKEN = local_settings.DISCORD_TOKEN
    GUILD = local_settings.DISCORD_GUILD

    client = discord.Client()

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    @client.event
    async def on_message(message):
        if message.content.lower().startswith('!roll '):

            try:
                holder = [int(i) for i in re.findall(r'\d+', message.content[6:])]
            except:
                await message.channel.send(f"Woah boy, that formatting duder. Example: !roll 2d8+4")

            if '+' in message.content:
                roll_list = roll(1, holder)
                await message.channel.send(f'You have rolled a {roll_list[-1]} on {holder[0]} x d{holder[1]}s + {holder[2]}')
            elif '-' in message.content:
                roll_list = roll(2, holder)
                await message.channel.send(f'You have rolled a {roll_list[-1]} on {holder[0]} x d{holder[1]}s - {holder[2]}')
            elif len(holder) == 2:
                roll_list = roll(0, holder)
                await message.channel.send(f'You have rolled a {roll_list[-1]} on {holder[0]} x d{holder[1]}s')
            else:
                num = basic_roll(holder)
                await message.channel.send(f'You have rolled a {num} on a d{holder[0]}')

        if message.content.lower().startswith('!rollout'):
            try:
                holder = [int(i) for i in re.findall(r'\d+', message.content[6:])]
            except:
                await message.channel.send(f"Woah boy, that formatting duder. Example: !rollout 5d20")

            roll_list = roll(0, holder)
            for i in roll_list[:-1]:
                await message.channel.send(f'You have rolled a {i} total on a d{holder[1]}')
            await message.channel.send(f'You have rolled a total of {roll_list[-1]} on {holder[0]} x d{holder[1]}s')

        if message.content.lower().startswith('!help'):
            await message.channel.send(f"Examples: !roll 20, !roll 2d12, !roll 3d8+5, !roll 2d6-5, !rollout 5d20")

    client.run(TOKEN)
