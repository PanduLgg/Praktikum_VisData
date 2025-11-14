import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

#Map
st.title('Map')
locate_map = pd.DataFrame(
    np.random.randn(50, 2)/[10, 10] + [15.4589, 75.0078],
    columns=['lat', 'lon']
)
st.map(locate_map)