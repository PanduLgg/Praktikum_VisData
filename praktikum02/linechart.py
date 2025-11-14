import streamlit as st
import pandas as pd
import numpy as np

#Line_Chart
st.title('Line Chart')
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)
st.line_chart(df)