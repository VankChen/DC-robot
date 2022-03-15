import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="")

@bot.event
async def on_ready():
    print("Bot is online")

bot.run("OTUzMTM0MTk1MDg4MTk1NjI1.YjAJZA.13C6Av0thqd0CGE3o96VykQ6dlc")