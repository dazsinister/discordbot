import discord
from discord.ext import commands

from apikey import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the Comic bot how can I help you?")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye, hope you have a good rest of the day")


async def help(ctx):
    await ctx.send("Avialble commands are as followed,"
                  "/!help",
                  "/!hello",
                  "/!goodbye")

@client.event
async def on_member_join(member):
    channel = client.get_channel(442444744464007190)
    await channel.send("Welcome to ShotPVP!")

@client.event
async def on_memeber_remove(member):
    channel = client.get_channel(442444744464007190)
    await channel.send("Goodbye, you will be missed")

client.run(TOKEN)