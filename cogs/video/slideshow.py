import os
import discord
from discord.ext import commands
import discord.types
from classes.slidshow_builder import SlideShowBuilder

class SlideShow(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="slideshow", description="Create a slideshow from images.")
  async def slideshow(
    self, 
    ctx: commands.Context
  ):
    message = ctx.message
    attachments: list[discord.Attachment] = message.attachments
    slide_show = SlideShowBuilder()

    for attachment in attachments:
      if attachment.content_type.startswith('image/'):
        slide_show.add_image_clip(await attachment.read())

      if attachment.content_type.startswith('audio/'):
        slide_show.add_audio(await attachment.read())

    file_path = await slide_show.generate_slide_show(f"{message.id}-{ctx.author.id}")
    file = discord.File(open(file_path, 'rb'))

    await ctx.send(file=file)
    os.remove(file_path)


def setup(bot):
  bot.add_cog(SlideShow(bot))