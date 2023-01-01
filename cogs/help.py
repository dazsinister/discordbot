#imports
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    #this is the wip help command
    # slash commands
    testServerId = 442444744464007188

    @nextcord.slash_command(name="help", description="This is here to help you", guild_ids=[testServerId])
    async def help(self, interaction: Interaction):
        await interaction.response.send_message("Hello, how can I help you? If you are looking for commands try / commands")

def setup(client):
    client.add_cog(help(client))