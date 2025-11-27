import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Praktikum 04 Visualisasi Data")
st.subheader("Bar Chart Filter")
st.markdown("""
1. Pandu Linggar - 0110220217
2. Silvia Pitriani - 0110222136
3. Rochmad Bima Setyawan - 0110122152
""")

#Data
data = {
    'Tahun' : ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer' : [100, 110, 120, 130, 140],
    'Sistem Informasi' : [120, 125, 135, 145, 160],
    'Teknik Informatika' : [90, 95, 100, 105, 110],
    'Data Science' : [70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

st.title('Trend Line Chart Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)')
filter_tahun = st.multiselect('Pilih Tahun', df['Tahun'], default=df['Tahun'])

jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect('Pilih Jurusan', jurusan_list, default=jurusan_list)

# Filter DataFrame berdasarkan pilihan pengguna
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]
# Menampilkan Data Table
st.subheader('Data Jumlah Mahasiswa per Tahun')
st.dataframe(filtered_data)

#Membuat Bar Chart dengan Filter
st.subheader('Bar Chart dengan Filter')
fig, ax = plt.subplots(figsize=(10, 6))

x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

#Sumbu dan Judul
ax.set_title('Jumlah Mahasiswa per Jurusan Bedasarkan Filter')
ax.set_xlabel('Tahun')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

st.pyplot(fig)