import streamlit as st
import numpy as np
import time

#Sidebar
st.sidebar.title('Sidebar Example')
st.sidebar.radio('Are You New User?',['Yes','No'])
st.sidebar.slider('Select Your Number',0,10)