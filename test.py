from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file

import os # default module
import constants
from classes.factories.clip_factory import ClipFactory
from classes.slidshow_builder import SlideShowBuilder
import random
from moviepy import vfx
import asyncio

async def main() -> None:

  slideshow_builder = SlideShowBuilder()

  for i in range(5):
    clip = ClipFactory.random_clip(duration=random.randint(5, 15)).generate_video_clip()
    slideshow_builder.add_clip(clip)
    # clip.write_videofile(f"./storage/temp/OUTPUT-clip{i}.mp4")


  await slideshow_builder.generate_slide_show('OUTPUT-slideshow')

if __name__ == '__main__':
  asyncio.run(main())