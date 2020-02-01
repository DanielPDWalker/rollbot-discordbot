# bot.py
import os

import discord
from dotenv import load_dotenv
import local_settings

load_dotenv()
token = local_settings.token

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
