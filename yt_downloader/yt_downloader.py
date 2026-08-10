import yt_dlp

url = input("Enter YouTube URL: ")
folder = input("Enter download folder path: ")

options = {
    "format": "best[ext=mp4]/best",
    "outtmpl": folder + "/%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")
