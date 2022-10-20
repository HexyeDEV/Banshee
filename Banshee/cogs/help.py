from discord.ext import commands
import discord
from discord import app_commands

class help(commands.Cog):
    def __init__(self,client):
        self.client=client

    @app_commands.command(name="help", description="Show list of commands.")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Help Command", description="Banshee's commands")
        embed.add_field("/basement <user>", "Send someone to my basement")
        embed.add_field("/prank", "Send a prank to the server.")
        embed.add_field("/sounds scary", "Play a scary sound.")
        embed.add_field("/sounds loud", "Play a loud sound.")
        embed.add_field("/sounds horrifying", "Play an horrifying sound.")
        embed.add_field("/sounds shiver", "Play a shiving sound.")
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(help(client))