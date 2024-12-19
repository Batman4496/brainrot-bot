from classes.clip import Clip, ClipObject, PositionedClipObject
from moviepy import (
  VideoClip, 
  concatenate_videoclips, 
  CompositeVideoClip, 
  VideoFileClip,
  ImageClip
)
from constants import DEFAULT_CLIP_DURATION, CLIP_TYPE


class ClipBuilder:

  def __init__(self):
    self.clip: Clip = Clip(
      fillers=[],
      duration=DEFAULT_CLIP_DURATION
    )

  def setResolution(self, width: int, height: int):
    self.clip.size = (width, height)
    return self

  def set_background(self, data: str, type: CLIP_TYPE, effects = [], duration = DEFAULT_CLIP_DURATION):
    background = ClipObject(
      type=type,
      value=data,
      duration=duration,
      effects=effects,
      start=None
    )

    self.clip.background = background
    self.clip.duration = duration
    return self
  
  def add_filler(
      self, 
      data: str, 
      type: CLIP_TYPE,
      position: tuple[int, int], 
      size: tuple[int, int], 
      effects = [], 
      duration = DEFAULT_CLIP_DURATION,
      start = None
    ):
    if duration > self.clip.duration:
      raise "Duration cannot be longer than clip itself"
    
    filler = PositionedClipObject(
      value=data,
      type=type,
      duration=duration,
      size=size,
      position=position,
      effects=effects,
      start=start
    )

    self.clip.fillers.append(filler)
    return self

    
  def get_duration(self):
    return self.clip.duration or DEFAULT_CLIP_DURATION

  def get_video_clip(self) -> VideoFileClip | ImageClip:
    if self.clip.background.type == 'image':
      main_video = ImageClip(self.clip.background.value)
    else:
      main_video = VideoFileClip(self.clip.background.value)
    
    if main_video.duration and self.get_duration():
      duration = self.get_duration() if self.get_duration() < main_video.duration else main_video.duration
    else:
      duration = DEFAULT_CLIP_DURATION
      self.clip.duration = duration

    main_video = main_video.resized(self.clip.size)
    main_video = main_video.with_duration(duration)

    return main_video

  def generate_video_clip(self) -> VideoClip | CompositeVideoClip:
    if not self.clip.duration:
      raise "No clips found."
    
    main_video = self.get_video_clip()

    filler_array = []

    for filler in self.clip.fillers:
      if filler.type == 'image':
        f = ImageClip(filler.value)
      else:
        f = VideoFileClip(filler.value)

      if filler.duration and f.duration:
        duration = (filler.duration if filler.duration < f.duration else f.duration)
      else:
        duration = DEFAULT_CLIP_DURATION
        filler.duration = duration

      f = f.with_duration(duration)
      
      if filler.size:
        f = f.resized(width=filler.size[0], height=filler.size[1])

      if filler.position:
        f = f.with_position(pos=filler.position)
      
      if filler.start:
        f = f.with_start(filler.start)

      filler_array.append(f)

    composite = CompositeVideoClip([main_video, *filler_array])
    composite = composite.with_duration(main_video.duration)
    
    return composite


    
