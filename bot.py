# bot.py
import discord
import local_settings

token = local_settings.DISCORD_TOKEN
guild = local_settings.DISCORD_GUILD

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
