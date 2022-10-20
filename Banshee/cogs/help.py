from discord.ext import commands
import discord
from discord import app_commands

class help(commands.Cog):
    def __init__(self,client):
        self.client=client

    @app_commands.command(name="help", description="Show list of commands.")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Help Command", description="Banshee's commands")
        embed.add_field(name="/basement <user>", value="Send someone to my basement")
        embed.add_field(name="/prank", value="Send a prank to the server.")
        embed.add_field(name="/sounds scary", value="Play a scary sound.")
        embed.add_field(name="/sounds loud", value="Play a loud sound.")
        embed.add_field(name="/sounds horrifying", value="Play an horrifying sound.")
        embed.add_field(name="/sounds shiver", value="Play a shiving sound.")
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(help(client))