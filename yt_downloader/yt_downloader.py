import gradio as gr
import yt_dlp
import os

def download_video(url):
    if not url:
        return "Please enter a YouTube URL."

    folder = "downloads"
    os.makedirs(folder, exist_ok=True)

    try:
        options = {
            "format": "best[ext=mp4]/best",
            "outtmpl": os.path.join(folder, "%(title)s.%(ext)s")
            
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return "Video downloaded successfully!"

    except Exception as e:
        return f"Error: {e}"


app = gr.Interface(
    fn=download_video,
    inputs=gr.Textbox(label="YouTube URL"),
    outputs=gr.Textbox(label="Status"),
    title="YouTube Video Downloader"
)

app.launch()
