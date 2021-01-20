from dotenv import load_dotenv
from pathlib import Path
import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.startswith
    msg1 = message.channel.send
    if msg('who'):
        await msg1("happy birthday saibaba coded discord bot for u - mayank")


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client.run(os.environ['AUTH_TOKEN'])
