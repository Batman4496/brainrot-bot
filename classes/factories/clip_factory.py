from random import randint, choice
from classes.clip_builder import ClipBuilder
from classes.memer import Memer

class ClipFactory:

  @staticmethod
  def random_clip(duration = 10, total_clips = 4) -> ClipBuilder:
    builder = ClipBuilder()
    c = choice(['videos', 'pictures'])
    builder.set_background(
      data=Memer.get_random(c),
      type=('video' if c == 'videos' else 'image'),
      duration=duration
    )

    vide = builder.get_video_clip()
    for _ in range(total_clips):
      c = choice(['videos'])
      builder.add_filler(
        Memer.get_random(c),
        type=('video' if c == 'videos' else 'image'),
        position=(randint(0, vide.w - int(vide.w // 10)), randint(0, vide.h - int(vide.h // 10))),
        size=(randint(100, vide.w // 2), randint(100, vide.h // 2)),
        duration=randint(1, int(vide.duration)),
        start=randint(0, vide.duration // 2)
      )

    return builder
