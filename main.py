import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]

from colors import clr

from diffusion import Diffusion

print('\n' + clr.cyan + '  TOC_BOT RUNNNING... \n' + clr.clear)

import discord
import re

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

_diffusion = Diffusion()


@client.event
async def on_ready():
    print(clr.bold + '  We have logged in as {0.user}'.format(client) + clr.clear)

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!image'):
        match = re.search(r"!image (.*)", message.content)

        x = f'{match}'
        print(x)
        image_sending = _diffusion.run('new', x)

        await message.channel.send(file=discord.File('new.jpg'))


client.run(DISCORD_TOKEN)
