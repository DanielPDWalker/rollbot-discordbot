# bot.py
import discord
import local_settings
import random as r
import re

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
    if message.content.startswith('!roll'):

        holder = re.findall(r'\d+', message.content)

        try:
            number = int(holder[0])
        except ValueError:
            await message.channel.send("Please use a numberino frienderino.")

        await message.channel.send(f'You have rolled a {r.randint(0,number)} on a d{number}')


client.run(TOKEN)
