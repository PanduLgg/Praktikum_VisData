import streamlit as st
import numpy as np
import time
from PIL import Image

#Define two columns
st.title('Display Image in Columns')
col1, col2 = st.columns(2)
# Inserting Element in column 1
col1.write("This is Column 1")
col1.image('C:/Kuliah/SEM 7/Visdata/Praktikum/praktikum02/assets/background.jpg')
# Inserting Element in column 2
col2.write("This is Column 2")
col2.image('C:/Kuliah/SEM 7/Visdata/Praktikum/praktikum02/assets/image.png')

#Space-Out between columns
img = Image.open('C:/Kuliah/SEM 7/Visdata/Praktikum/praktikum02/assets/background.jpg')
st.title('Image with Space Out')
#Defineing 2 Columns with space out
for _ in range(2):
    cols = st.columns([3,1,2,1])
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

#Column with Padding
st.title('Column with Padding')
img = Image.open('C:/Kuliah/SEM 7/Visdata/Praktikum/praktikum02/assets/image.png')
col1, padding, col2 = st.columns([10,2,10])
with col1:
    col1.image(img)
with col2:
    col2.image(img)

#Grid of Images using Columns
img = Image.open('C:/Kuliah/SEM 7/Visdata/Praktikum/praktikum02/assets/image.png')
st.title('Grid')
#rows
for a in range(4):
    cols = st.columns((1,1,1,1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

#Expanders
st.title('Expanders')
with st.expander("Streamlit with Python"):
    st.write("""Develop ML Applications in minute!!!!""")

#Containers
st.title('Containers')
with st.container():
    st.write("This is inside the container")
    st.line_chart(np.random.randn(40, 4))
    st.write("This is outside the container")

st.title('Out of Order Container')
container_one = st.container()
container_one.write("This is the first container")
st.write("This is outside the container")
#Insert Element in container_one
container_one.write("This is Element 2 the inside container")
container_one.line_chart(np.random.randn(40, 4))

#Empty Container
st.title('Empty Container')
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ Loading... {seconds} seconds have passed")
        time.sleep(1)
        st.write("✔️ Times Up!") 

