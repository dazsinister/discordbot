#imports
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    # slash commands
    testServerId = 442444744464007188

    @nextcord.slash_command(name="hello", description="A nice greeting", guild_ids=[testServerId])
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message("Hello and welcome! Glad to have you here!")

    @nextcord.slash_command(name="goodbye", description="A friendly goodbye", guild_ids=[testServerId])
    async def goodbye(self, interaction: Interaction):
        await interaction.response.send_message("Goodbye and thanks for joining us. Hope to see you again")


def setup(client):
    client.add_cog(Greetings(client))