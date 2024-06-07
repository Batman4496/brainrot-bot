from ffmpeg import FFmpeg



def main() -> None:
  process = (
    FFmpeg("./storage/ffmpeg/ffmpeg.exe")
    .option("y")
    .input("./storage/inflex.mp4")
    .output("./storage/output.mp4", {
      '-filter:v': 
    })
  )

  process.execute()

if __name__ == '__main__':
  main()