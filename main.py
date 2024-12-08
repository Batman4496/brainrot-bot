from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file

import discord
from discord.ext import commands
import os # default module
import constants

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(command_prefix="~", intents=intents)

@bot.event
async def on_ready() -> None:
  print("READY!!!") 

@bot.slash_command(description="Say Hi!")
async def hello(ctx):
  await ctx.respond("Hello!")

for cog in constants.COGS:
  bot.load_extension(f'cogs.{cog}')
  print(cog, "loaded!")

bot.run(os.environ.get("TOKEN")) # run the bot with the token