from discord.ext import commands
import discord
from discord import app_commands
import asyncio

class sounds(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    sounds = app_commands.Group(name="sounds", description="Play noises in your current voice channel")

    @sounds.command(name="loud", description="Play a Loud Noise")
    async def loud(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.voice_channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Loud Noise in {channel}. 🎃", ephemeral=True)
            vc = await self.client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('./assets/loud.mp3', after=lambda: print('done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1.5)
            player.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃", ephemeral=True)

    @sounds.command(name="scary", description="Play a Scary Sound")
    async def scary(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.voice_channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Scary Sound in {channel}. 🎃", ephemeral=True)
            vc = await self.client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('./assets/scary.mp3', after=lambda: print('done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1.5)
            player.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃", ephemeral=True)

    @sounds.command(name="horrifying", description="Play an Horrifying Sound")
    async def horrifying(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.voice_channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Horrifying Sound in {channel}. 🎃", ephemeral=True)
            vc = await self.client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('./assets/horrifying.mp3', after=lambda: print('done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1.5)
            player.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃 ", ephemeral=True)

    @sounds.command(name="shiver", description="Play an Shiving Sound")
    async def shiver(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.voice_channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Shiving Sound in {channel}. 🎃", ephemeral=True)
            vc = await self.client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('./assets/shiving.mp3', after=lambda: print('done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1.5)
            player.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃", ephemeral=True)


async def setup(client):
    await client.add_cog(sounds(client))