from dataclasses import dataclass, field
from constants import CLIP_TYPE, DEFAULT_CLIP_SIZE
from moviepy.Effect import Effect

@dataclass
class ClipObject:
  value: str
  type: CLIP_TYPE
  effects: list[Effect]
  duration: int
  start: int = field(default=None)

@dataclass
class PositionedClipObject(ClipObject):
  position: tuple[int, int] = field(default=None)
  size: tuple[int, int] = field(default=None)

@dataclass
class Clip:
  background: ClipObject = field(default=None)
  fillers: list[PositionedClipObject] = field(default=None)  # Random images/videos
  audio: ClipObject = field(default=None)
  duration: int = field(default=None)
  size: tuple[int, int] = field(default=DEFAULT_CLIP_SIZE)