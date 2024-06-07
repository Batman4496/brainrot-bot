import os
import discord
import discord.ui as UI

class WatchView:

  def __init__(self, movie: str, chunk: str) -> None:
    self.movie = movie
    self.chunk = int(chunk)
    self.watching = False
    self.chunks = None


  def getMovieChunks(self) -> list:
    return os.listdir(f"./storage/chunks/{self.movie}")

  def generate_embed(self):
    embed = discord.Embed(title=self.movie)

    if not self.chunks:
      self.chunks = self.getMovieChunks()

    embed.set_footer(text=f"Chunk {self.chunk}/{len(self.chunks)}")

    return embed
    

  def generate_file(self):
    if not self.watching:
      return None
    
    file = discord.File(f"./storage/chunks/{self.movie}/{self.chunks[self.chunk]}")
    return file

  async def next_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    if (self.chunk + 1) >= len(self.chunks):
      self.chunk = 0
    else:
      self.chunk += 1

    await interaction.followup.edit_message(
      interaction.message.id,
      embed=self.generate_embed(), 
      view=self.generate_view(), 
      file=self.generate_file()
    )


  async def prev_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    if (self.chunk - 1) < 0:
      self.chunk = len(self.chunks) - 1
    else:
      self.chunk -= 1

    await interaction.followup.edit_message(
      interaction.message.id,
      embed=self.generate_embed(), 
      view=self.generate_view(), 
      file=self.generate_file()
    )

  async def watch_callback(self, interaction: discord.Interaction):
    await interaction.response.defer()
    self.watching = True
    await interaction.followup.edit_message(
      interaction.message.id,
      embed=self.generate_embed(), 
      view=self.generate_view(), 
      file=self.generate_file()
    )

  def generate_view(self):
    view = UI.View()

    if not self.watching:
      watch_button = UI.Button(label="Watch Now")
      watch_button.callback = self.watch_callback
      
      view.add_item(watch_button)    

      return view
    
    if self.chunk > 0:
      prev_button = UI.Button(label="Prev")
      prev_button.callback = self.prev_callback
      view.add_item(prev_button)
    
    if self.chunk < len(self.chunks):
      next_button = UI.Button(label="Next")
      next_button.callback = self.next_callback
      view.add_item(next_button)

    return view

