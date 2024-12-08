import moviepy
from moviepy import ImageClip, Effect, VideoClip, AudioClip
from constants import TEMP_PATH

class SlideShowBuilder:

  def __init__(self):
    self.clips: list[VideoClip] = []
    self.audio: moviepy.AudioClip = None
    self.duration = 0

  def add_image_clip(self, path: str, effects: list[Effect] = [], duration = 2):
    clip = ImageClip(path)

    if len(effects) > 0:
      clip = clip.with_effects(effects)
    
    clip = clip.with_duration(duration)
    self.duration += duration
    self.clips.append(clip)
    
    return self

  def add_audio(self, path: str):
    self.audio = path
    return self
  
  def add_clip(self, clip: any):
    self.clips.append(clip)
    self.duration += clip.duration
    return self

  async def generate_slide_show(self, filename: str):
    final_clip = moviepy.concatenate_videoclips(self.clips, method="compose")
    final_clip.write_videofile(TEMP_PATH + f'/{filename}.mp4', fps=24)

    return TEMP_PATH + f'/{filename}.mp4'