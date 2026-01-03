import streamlit as st
from PIL import Image # pip install pillow

st.title("color to greyscale image converter")


def show_greyscale(image_file):
    """Open an image file-like object, convert to greyscale and display it."""
    img = Image.open(image_file)
    greyscale_img = img.convert("L")
    st.image(greyscale_img)


Uploaded_image = st.file_uploader("Upload an image", 
                                  type=["png", "jpg", "jpeg"])
if Uploaded_image:
    show_greyscale(Uploaded_image)

with st.expander("Camera Input"):
    camera_image = st.camera_input("Take a picture")

if camera_image:
    show_greyscale(camera_image)
