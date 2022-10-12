from discord.ext import commands
import discord

class on_join(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send("Banshee's here!", file=discord.File("./assets/banshee.gif"))
                break
        else:
            print(f"The guild {guild.id} has no channel where I have send_messages permission.")

async def setup(client):
    await client.add_cog(on_join(client))