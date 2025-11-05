import streamlit as st
import base64
from PIL import Image

st.write("Displaying an Image")
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")
st.write("Image Courtesy: Streamlit")

st.write("Displaying Multiple Images")
animal_images = [
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1517423440428-a5a00ad493e8",
    "https://images.unsplash.com/photo-1500534623283-312aade485b7"
]
st.image(animal_images, width=150)
st.write("Images Courtesy: Unsplash")

def add_local_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
add_local_background_image("C:/Kuliah/SEM 4/VISDATA/Project/praktikum01/background.jpg")

original_image = Image.open("C:/Kuliah/SEM 4/VISDATA/Project/praktikum01/background.jpg")
st.title("Original Image Display")
st.image(original_image, caption="Original Background Image")
resized_image = original_image.resize((600, 400))
st.title("Resized Image Display")
st.image(resized_image, caption="Resized Background Image (600x400)")