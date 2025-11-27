import matplotlib.pyplot as plt
import streamlit as st

st.title("Praktikum 03 Visualisasi Data")
st.subheader("Line Chart dengan Matplotlib")
st.markdown("""
1. Pandu Linggar - 0110220217
2. Rizky Amalia - 0110220218
3. Salsabila Putri - 0110220222
""")

#DATA SAMPLE
months = ('Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20,22, 30, 25, 35, 40, 45]
product_C_sales = [18, 22, 25, 28, 32, 38, 42, 45, 48,52, 56, 60]
product_D_sales = [7, 9, 11, 13, 16, 18,20, 22, 24, 26, 28, 30]

#Streamlit Layout
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", 
                              ("Line Plot", 
                               "Kustomisasi Line Plot", 
                               "Garis Berbeda Menunjukkan Trend", 
                               "SubPlot"))

def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title("Penjualan Produk A per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penjualan")
    st.pyplot(fig)

def customized_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, color='blue', marker='o', linestyle='--')
    ax.plot(months, product_B_sales, color='red', marker='x', linestyle='-')
    ax.set_title("Penjualan Produk per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penjualan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def trend_lines():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Produk A', color='blue')
    ax.plot(months, product_B_sales, label='Produk B', color='red')
    ax.plot(months, product_C_sales, label='Produk C', color='green')
    ax.plot(months, product_D_sales, label='Produk D', color='purple')
    ax.set_title("Trend Penjualan Produk per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penjualan")
    ax.legend()
    st.pyplot(fig)

def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))  

    #Plot Product A
    axs[0].plot(months, product_A_sales, color='blue', marker='o')
    axs[0].set_title("Penjualan Produk A per Bulan")
    axs[0].set_xlabel("Bulan")
    axs[0].set_ylabel("Jumlah Penjualan")
    axs[0].legend()
    axs[0].grid(True)

    #Plot Product B
    axs[1].plot(months, product_B_sales, color='red', marker='x')
    axs[1].set_title("Penjualan Produk B per Bulan")
    axs[1].set_xlabel("Bulan")
    axs[1].set_ylabel("Jumlah Penjualan")
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customized_line_plot()
elif option == "Garis Berbeda Menunjukkan Trend":
    trend_lines()
elif option == "SubPlot":
    subplots()