import streamlit as st
# Page Settings

st.set_page_config(
    page_title="My Music",
    page_icon="🎵",
    layout="wide"
)
# Background Image 

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/shubhamverma2026-ai/music-app/e088e33db7fbf9906e15d853e7d80cd09d253e02/background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .spotify-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 220px;
    }
    </style>
    """,
    unsafe_allow_html=True
)




playlist_url = "https://open.spotify.com/embed/playlist/4HGxkMbaqCbHetmy0Qd4Xc"

st.markdown(
    f"""
    <div class="spotify-container">
        <iframe
            src="{playlist_url}"
            width="600"
            height="152"
            frameborder="0"
            allowtransparency="true"
            allow="encrypted-media"
            style="border-radius: 12px;">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)
