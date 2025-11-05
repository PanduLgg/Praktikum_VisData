import streamlit as st
import pandas as pd 
import numpy as np #data numerik acak
import altair as alt #chart

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 2: Data Elements")
st.markdown("""
1. Pandu Linggar - 0110220217
2. Rizky Amalia - 0110220218
3. Salsabila Putri - 0110220222
""")

st.subheader("Data Frame")
#Membuat Data Frame

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=['col_no %d' % i for i in range(10)]
)
#Menampilkan Data Frame
st.dataframe(df)

#Highlighting Nilai Minimum dan Maksimum
st.subheader("Highlighting Nilai Minimum")
st.dataframe(
    df.style.highlight_min(axis=0)
)

st.subheader("Highlighting Nilai Maksimum")
st.dataframe(
    df.style.highlight_max(axis=0)
)


#Tabel Statis
st.subheader("Tabel Statis")
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=['col %d' % i for i in range(5)]
)
st.table(df)

#Metrics
st.subheader("Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", "25 °C", "1.2 °C")
with col2:
    st.metric("Humidity", "60 %", "-3 %")
with col3:
    st.metric("Wind Speed", "15 km/h", "2 km/h")

#Metric Delta Color
st.subheader("Metric Delta Color")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sales", "$1,000", "5 %", delta_color="normal")
with col2:
    st.metric("Populasi", "123 Miliar", "1 Miliar", delta_color="inverse")
with col3:
    st.metric("Pelanggan", "100", "0", delta_color="off")


#Chart Altair
st.subheader("Chart Altair")
chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['x', 'y', 'category']
)
chart = alt.Chart(chart_data).mark_circle(size=60).encode(
    x='x',
    y='y',
    color='category',
    tooltip=['x', 'y', 'category']
).interactive()
st.altair_chart(chart, use_container_width=True)

#LINE CHART
st.subheader("Chart Garis Sederhana")
line_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['x', 'y']
)
line_chart = alt.Chart(line_data).mark_line().encode(
    x='x',
    y='y'
).interactive()
st.altair_chart(line_chart, use_container_width=True)

#BAR CHART
st.subheader("Chart Batang Sederhana")
bar_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['category', 'value']
)
bar_chart = alt.Chart(bar_data).mark_bar().encode(
    x='category',
    y='value'
).interactive()
st.altair_chart(bar_chart, use_container_width=True)