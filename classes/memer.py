import os
import random
from constants import MEME_FOLDER, MEME_TYPE

class Memer:
  @staticmethod
  def get_random(type: MEME_TYPE):
    dir = os.listdir(f"{MEME_FOLDER}/{type}")
    choice = random.choice(dir)

    return MEME_FOLDER + f"/{type}/{choice}"
  


if __name__ == '__main__':
  Memer.get_random('songs')