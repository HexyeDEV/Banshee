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
        voice_channel=user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Loud Noise in {channel}. 🎃", ephemeral=True)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio("./assets/loud.mp3"), after=lambda: print('done'))
            while vc.is_playing():
                await asyncio.sleep(1.5)
            vc.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃", ephemeral=True)

    @sounds.command(name="scary", description="Play a Scary Sound")
    async def scary(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Loud Noise in {channel}. 🎃", ephemeral=True)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio("./assets/scary.mp3"), after=lambda: print('done'))
            while vc.is_playing():
                await asyncio.sleep(1.5)
            vc.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃", ephemeral=True)

    @sounds.command(name="horrifying", description="Play an Horrifying Sound")
    async def horrifying(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Loud Noise in {channel}. 🎃", ephemeral=True)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio("./assets/horrifying.mp3"), after=lambda: print('done'))
            while vc.is_playing():
                await asyncio.sleep(1.5)
            vc.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃 ", ephemeral=True)

    @sounds.command(name="shiver", description="Play an Shiving Sound")
    async def shiver(self, interaction: discord.Interaction):
        user = interaction.user
        voice_channel=user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await interaction.response.send_message(f"🎃 Playing Loud Noise in {channel}. 🎃", ephemeral=True)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio("./assets/shiver.mp3"), after=lambda: print('done'))
            while vc.is_playing():
                await asyncio.sleep(1.5)
            vc.stop()
            await vc.disconnect()
        else:
            await interaction.response.send_message("🎃 You are not in a voice channel 🎃", ephemeral=True)


async def setup(client):
    await client.add_cog(sounds(client))