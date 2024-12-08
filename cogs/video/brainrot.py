import os
import discord
from discord.ext import commands
import discord.types
from classes.slidshow_builder import SlideShowBuilder
from classes.factories.clip_factory import ClipFactory
from classes.helper import delete_file 

class BrainRot(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name="brainrot", description="Create brainrot.")
  async def brainrot(
    self, 
    ctx: discord.ApplicationContext,
    duration: discord.Option(
      int,
      description="Brainrot per second(s)",
      default=10,
      max_value=20
    ),
    clips: discord.Option(
      int,
      description="Number of brainrot clips",
      default=4,
      max_value=10
    ),
  ):
    try:
      await ctx.response.defer()
      await ctx.followup.send("***Generating brainrot... Please wait...***")
      slideshow = SlideShowBuilder()
      factory = ClipFactory()
    
      for _ in range(clips):
        clip = factory.random_clip(duration)
        slideshow.add_clip(clip.generate_video_clip())

      filename = f"{ctx.followup.id}-{ctx.author.id}"
      file_path = await slideshow.generate_slide_show(filename)

      file = discord.File(open(file_path, 'rb'))
      await ctx.send("***brainrot.mp4***", file=file)

    except Exception as e:
      await ctx.send(f"**An error occured!!**\n```{e}``")

    finally:
      await delete_file(file_path)

def setup(bot):
  bot.add_cog(BrainRot(bot))