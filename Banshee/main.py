import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiosqlite
import logging

discord.utils.setup_logging()

load_dotenv()
token = os.getenv("TOKEN")

class MyBot(commands.Bot):
    def __init__(self):
            super().__init__(
            command_prefix="b!",
            intents=discord.Intents.all(),
            application_id=1028707610238668851,
            activity=discord.Game(name="/help"),
        )
    
    async def on_ready(self):
        print(f"Logged in As {self.user}")

    async def setup_hook(self):
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file.replace('.py', '')}")
        for file in os.listdir("./events"):
            if file.endswith(".py"):
                await self.load_extension(f"events.{file.replace('.py', '')}")
client = MyBot()

async def main():
    async with client:
        await client.start(token)

asyncio.run(main())