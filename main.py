import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.all())

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.command()
async def hi(ctx):
  channel = ctx.message.channel
  await channel.send(f"hi {ctx.author.name}!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
keep_alive()
client.run('MTE0NjE0NTI0MjE0ODUwNzY1OA.GnHY5W.KDIA58x74hGJwPTlB-Ci8HWGJjefIPfQpqylRs')