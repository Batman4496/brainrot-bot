import os
import discord
from discord.ext import commands
from views.watch_view import WatchView

class Watch(commands.Cog):

  def __init__(self, bot: discord.Client) -> None:
    self.bot = bot

  @commands.slash_command(name="watch", description="Watch Movie")
  async def watch(
    self, 
    ctx: discord.ApplicationContext, 
    movie: discord.Option(
        name="name",
        description="Movie name",
        required=True,
        choices=os.listdir('./storage/chunks'),
    ),
    chunk: discord.Option(
      name="chunk",
      description="Chunk id you want to watch (i.e. 0-n).",
      default=0
    )
  ):
    await ctx.defer()
    if movie not in os.listdir('./storage/chunks'):
      return ctx.respond(f"Movie `{movie}` not found!")
    
    watch_view = WatchView(movie, chunk if chunk else 0)

    return await ctx.followup.send(
      view=watch_view.generate_view(), 
      embed=watch_view.generate_embed(),
    )

def setup(bot: discord.Client):
  bot.add_cog(Watch(bot))