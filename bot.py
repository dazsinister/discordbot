#imports
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
from apikey import *

#permissions for discord bot to work
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix= '!', intents=intents)

#printing out that the bot is ready to go if successful
@client.event
async def on_ready():
    await client.change_presence(status= nextcord.Status.idle, activity=nextcord.Game('Running life'))
    print("The bot is now ready for use!")
    print("-----------------")

#importing all the cogs into the bot
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

#for loop
if __name__=='__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

#run with token
client.run(TOKEN)
