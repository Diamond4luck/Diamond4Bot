import discord
import asyncio
import requests
import os
from discord.ext.commands import Bot
from discord.ext import commands
import random


Client = discord.Client()
bot_prefix='!!'

@client.event
async def on_ready():
    print("Bot is ready!")
    
@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        await message.channel.send("2020 woohoo.")

                             
client.run(os.environ['TOKEN'])



