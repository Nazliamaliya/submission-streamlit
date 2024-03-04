import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv(r'D:\MBKM THINGS\BANGKIT\hour.csv')
    return df

df = load_data()

st.sidebar.title('Menu')
selected_page = st.sidebar.radio('Pilih Halaman:', ['Ringkasan Data', 'Trend Persewaan Sepeda Bulanan', 'Perbedaan Hari Kerja dan Tidak'])

if selected_page == 'Ringkasan Data':
    st.title('Ringkasan Data')
    st.write(df.describe())

elif selected_page == 'Trend Persewaan Sepeda Bulanan':
    st.title('Trend Persewaan Sepeda Bulanan')
    sewa_sepeda_bulanan = df.groupby('mnth')[['cnt', 'casual', 'registered']].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(sewa_sepeda_bulanan.index, sewa_sepeda_bulanan['cnt'], label='Total Penyewa', color='blue')
    plt.plot(sewa_sepeda_bulanan.index, sewa_sepeda_bulanan['casual'], label='Penyewa Casual', color='red', linestyle='--')
    plt.plot(sewa_sepeda_bulanan.index, sewa_sepeda_bulanan['registered'], label='Penyewa Terdaftar', color='green', linestyle='-.')
    plt.title('Trend Line Penyewaan Sepeda Bulanan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    st.pyplot(plt)

elif selected_page == 'Perbedaan Hari Kerja dan Tidak':
    st.title('Perbandingan Rata-Rata Penyewa : Hari Kerja Vs Hari Libur')
    avg_workingday_rentals = df[df['workingday'] == 1]['cnt'].mean()
    avg_non_workingday_rentals = df[df['workingday'] == 0]['cnt'].mean()

    st.write('Rata-rata Jumlah Sewa Sepeda pada Hari Kerja:', avg_workingday_rentals)
    st.write('Rata-rata Jumlah Sewa Sepeda pada Bukan Hari Kerja:', avg_non_workingday_rentals)

    labels = ['Hari Kerja', 'Bukan Hari Kerja']
    sizes = [avg_workingday_rentals, avg_non_workingday_rentals]
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightcoral'])
    ax1.set_title('Perbandingan Rata-rata Jumlah Sewa Sepeda: Hari Kerja vs Bukan Hari Kerja')
    ax1.axis('equal')  
    caption_text = "Persentase saat bukan hari kerja lebih besar dibandingkan saat hari kerja."
    plt.text(0.5, -0.5, caption_text, horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes, fontsize=10, color='gray')
    st.pyplot(fig1)