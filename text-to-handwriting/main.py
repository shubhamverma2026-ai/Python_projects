import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap

st.set_page_config(page_title="Text to Handwriting", page_icon="✍️")
st.title("✍️ Text to Handwriting Converter")

text = st.text_area("Enter your text:")

def create_handwriting_image(text):
    width, height = 800, 1000
    bg_color = (255, 255, 255)
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("handwriting.ttf", 28)
    pen_color = (25, 25, 160)  # blue gel pen color

    # Wrap wider so text fills the page width properly
    wrapped = textwrap.fill(text, width=60)

    draw.multiline_text((50, 50), wrapped, font=font, fill=pen_color, spacing=14)

    return img

if st.button("Generate"):
    if text.strip():
        img = create_handwriting_image(text)
        st.image(img, caption="Your handwritten note")

        img.save("output.png")
        with open("output.png", "rb") as f:
            st.download_button("Download Image", f, file_name="handwriting.png")
    else:
        st.warning("Please enter some text first!")
