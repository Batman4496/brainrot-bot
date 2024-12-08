import os
import discord
import discord.ui as UI
import views.modal

class SlideShowView:

  def __init__(self) -> None:
    self.images: str = []
    self.audio = None

  def generate_embed(self):
    embed = discord.Embed(title=self.movie)
    embed.add_field(name="SlideShow Creator.", value="Add files to the slideshow.")
    embed.add_field(name="Images", value=f"{"No images." if len(self.images) < 1 else len(self.images)}")
    return embed
    

  async def add_file_callback(self, interaction: discord.Interaction):
    await interaction.resposne.defer()
    
    await interaction.response.send_modal()

  def generate_file(self):
    ...

  def generate_view(self):
    view = UI.View()

    add_file_button = UI.Button(label="+ Add")
    add_file_button.callback = 
    return view

