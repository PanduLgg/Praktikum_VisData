import streamlit as st
import pandas as pd
import numpy as np

# MANDIRI
st.title("Praktikum 02 Visualisasi Data")
st.markdown("""
1. Pandu Linggar - 0110220217
2. Silvia Pitriani - 0110222136
3. Rochmad Bima Setyawan - 0110122152
""")

#Bar_Chart
st.title('Bar Chart')
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)
st.bar_chart(df)
