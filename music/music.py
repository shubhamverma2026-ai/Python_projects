import streamlit as st
import base64

# Page title 

st.set_page_config(
    page_title="My Music",
    page_icon="🎵",
    layout="wide"
)


def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .spotify-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 220px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_background("background.jpg")

# -----------------------------
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
