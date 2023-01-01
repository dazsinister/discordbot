#imports
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Releases(nextcord.ui.View):
    def __init__(self):
        super().__init__() #timeout = None
        self.value = None

    @nextcord.ui.button(label = "releases", style=nextcord.ButtonStyle.gray)
    async def newreleases(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message('Check out these new releases', ephemeral=False) # this makes it so either everyone or only the user can see the message
        self.value = True
        self.stop()

class UI(commands.Cog):

    def __init__(self, client):
        self.client = client

    testServerId = 442444744464007188

    @nextcord.slash_command(name = "button", description = "Where to see new releases", guild_ids=[testServerId])
    async def releases(self, interaction: Interaction):
        view = Newreleases()
        await interaction.response.send_message("Come check out new releases", view=view)
        await view.wait()

        if view.value is None:
            return

        else:
            print("Enjoy!")

def setup(client):
    client.add_cog(help(client))