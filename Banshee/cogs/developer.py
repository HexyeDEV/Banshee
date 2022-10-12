from discord.ext import commands
import discord

class developer(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="sync_commands")
    @commands.is_owner()
    async def sync_commands(self, ctx):
        await self.client.tree.sync()
        await ctx.reply("Done!")

async def setup(client):
    await client.add_cog(developer(client))