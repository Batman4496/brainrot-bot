import os
import asyncio

async def delete_file(path):
  asyncio.sleep(2)
  os.remove(path)