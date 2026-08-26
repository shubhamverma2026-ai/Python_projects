# 🎵 My Music


<img width="1917" height="906" alt="image" src="https://github.com/user-attachments/assets/6dac708d-1e6f-4a24-81f7-d0b14e17a96e" />


A simple and aesthetic **Streamlit music player interface** that displays a Spotify playlist over a custom background image.

The project uses **Streamlit, HTML/CSS, and Base64 encoding** to create a minimal music-themed web interface.

## ✨ Features

* 🎵 Spotify playlist embedded directly into the webpage
* 🖼️ Custom background image
* 🌐 Full-width Streamlit layout
* 🎨 Custom CSS styling
* 📍 Spotify player centered on the page
* 🔗 Easy to replace with your own Spotify playlist
* ⚡ Simple and lightweight implementation

## 🛠️ Technologies Used

* **Python**
* **Streamlit**

* **Base64**
* **Spotify Embed**


### Files

| File             | Description                              |
| ---------------- | ---------------------------------------- |
| `app.py`         | Main Streamlit application               |
| `background.jpg` | Background image used by the application |
| `README.md`      | Project documentation                    |

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/my-music.git
cd my-music
```

### 2. Install Streamlit

Make sure Python is installed on your system, then run:

```bash
pip install streamlit
```

### 3. Add the Background Image

Place your background image inside the project folder and name it:

```text
background.jpg
```

The application expects the image to be available in the same directory as `app.py`.

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

## 🎧 Changing the Spotify Playlist

The Spotify playlist is embedded using its Spotify Embed URL.

Find this line in `app.py`:

```python
playlist_url = "https://open.spotify.com/embed/playlist/4HGxkMbaqCbHetmy0Qd4Xc"
```

Replace it with your own Spotify playlist embed URL.

For example:

```python
playlist_url = "https://open.spotify.com/embed/playlist/YOUR_PLAYLIST_ID"
```

You can get the playlist ID from your Spotify playlist URL.

## 🖼️ Changing the Background

Replace:

```text
background.jpg
```

with your own image.

The application automatically converts the image into Base64 and applies it as the webpage background using CSS.

The background is configured to:

* Cover the entire screen
* Stay centered
* Avoid repeating
* Remain fixed while scrolling

## 🎨 How It Works

### 1. Streamlit Page Configuration

The application configures the page title, icon, and layout:

```python
st.set_page_config(
    page_title="My Music",
    page_icon="🎵",
    layout="wide"
)
```

### 2. Background Image

The `set_background()` function reads the image and converts it into Base64:

```python
with open(image_file, "rb") as file:
    encoded = base64.b64encode(file.read()).decode()
```

The encoded image is then inserted into CSS as a background image.

### 3. Spotify Embed

The Spotify playlist is displayed using an HTML `<iframe>`:

```html
<iframe
    src="..."
    width="600"
    height="152"
    frameborder="0"
    allowtransparency="true"
    allow="encrypted-media">
</iframe>
```

This allows the Spotify playlist player to appear directly inside the Streamlit application.

## 📌 Requirements

* Python 3.8 or newer
* Streamlit
* Internet connection
* A Spotify playlist
* A background image

## 🔮 Future Improvements

Possible improvements for future versions:

* 🎚️ Add volume controls
* 🌙 Add dark/light mode
* 🎨 Add animated visual effects
* 🎵 Allow users to select different playlists
* 📱 Improve mobile responsiveness
* ✨ Add music-themed animations
* 🖼️ Allow users to upload their own background

## 👨‍💻 Author

**Shubham**

Built with Python 🐍 + Streamlit ⚡ + Spotify 🎵

> *"Sometimes all you need is good music and a questionable amount of CSS."* 🙄🎧

## 📄 License

This project is available for educational and personal use.
