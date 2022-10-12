from discord.ext import commands
import discord
from discord import app_commands

class basement(commands.Cog):
    def __init__(self,client):
        self.client=client

    @app_commands.command(name="basement", description="Send someone to my basement.")
    @app_commands.checks.cooldown(1, 60*30, key=lambda i: (i.user.id))
    @app_commands.describe(user="The target user")
    async def basement(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.defer()
        await interaction.followup.send(f"🎃 {user.mention} visited my basement... and never came back 👀👀", file=discord.File("./assets/basement.gif"))
    
    @basement.error
    async def on_basement_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(f"🎃 {error} 🎃", ephemeral=True)
        else:
            print(error)

async def setup(client):
    await client.add_cog(basement(client))