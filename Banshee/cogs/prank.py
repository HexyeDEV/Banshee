from discord.ext import commands
import discord
from discord import app_commands
import random

class prank(commands.Cog):
    def __init__(self,client):
        self.client=client

    @app_commands.command(name="prank", description="Make a scary prank to the server.")
    @app_commands.checks.cooldown(1, 60*60, key=lambda i: (i.guild_id))
    async def prank(self, interaction: discord.Interaction):
        for channel in interaction.guild.text_channels:
            if channel.permissions_for(interaction.guild.me).send_messages:
                string = random.choice(["🎃 Banshee's watching y'all 👀👀", "🎃 Don't turn around, Banshee's watching ;)", "🎃 Don't you feel alone?", "🎃 Wanna play some games in Banshee's basement?", "🎃 Don't you feel a presence behind you?"])
                await channel.send(string, file="./assets/banshee.gif")
                break
        else:
            await interaction.response.send("🎃 Sadly, I'm not allowed to type in any of this server's channel... I'll have my revenge ;)")
        await interaction.response.defer()

async def setup(client):
    await client.add_cog(prank(client))