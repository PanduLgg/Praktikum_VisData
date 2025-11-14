import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

#Area_Chart
st.title('Area Chart')
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)
st.area_chart(df)