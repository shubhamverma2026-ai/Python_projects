# 🎵 My Music
url : https://nostalgic-music.streamlit.app/

<img width="1917" height="906" alt="image" src="https://github.com/user-attachments/assets/6dac708d-1e6f-4a24-81f7-d0b14e17a96e" />


# 🎵 My Music App

A simple Streamlit app that shows a custom background image with an embedded Spotify playlist player.

## Features
- Custom full-screen background image
- Embedded Spotify playlist player
- Clean, centered layout

## Requirements
- Python 
- Streamlit

## Installation

1. Clone this repo:
```bash
git clone https://github.com/shubhamverma2026-ai/music-app.git
cd music-app
```

2. Install Streamlit:
```bash
pip install streamlit
```

## Usage

Run the app with:
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## Customization

- **Change the background image:** replace the image URL inside the `.stApp` CSS block in `app.py`.
- **Change the playlist:** replace the `playlist_url` variable with your own Spotify embed link. You can get this from Spotify by clicking **Share → Embed playlist** on any playlist.

## Notes

- Make sure the GitHub repo hosting the background image is **public**, or the image won't load.
