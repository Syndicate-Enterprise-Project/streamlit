import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from model import model as data
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_option_menu import option_menu

data_modeling = data.load_data_modelling().copy()
data_modeling['cluster_kmeans'] = data_modeling['cluster_kmeans'].apply(lambda x: x + 1)

data_clean = data.load_data_clean()


def dataset(df):
    filter_options = ['cluster_kmeans', 'cluster_hc', 'Tipe Mobil', 'Warna', 'Sumber Penjualan', 'Harga (Rp)',
                      'Cara Pembayaran']
    selected_filters = st.multiselect("Pilih kolom untuk filter:", filter_options)

    if selected_filters:
        filtered_df = df.loc[:, selected_filters]
        filtered_df = filtered_df.drop(['cluster_hc'], axis=1)
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)


def display_kmeans(df):
    st.markdown(
        """
        <style>
        [data-testid="stMetricValue"] {
            font-size: 25px;
            font-weight: bold;
        }
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    cluster1 = df[df['cluster_kmeans'] == 1]
    total_cluster1 = cluster1['cluster_kmeans'].count()

    cluster2 = df[df['cluster_kmeans'] == 2]
    total_cluster2 = cluster2['cluster_kmeans'].count()

    cluster3 = df[df['cluster_kmeans'] == 3]
    total_cluster3 = cluster3['cluster_kmeans'].count()

    cluster4 = df[df['cluster_kmeans'] == 4]
    total_cluster4 = cluster4['cluster_kmeans'].count()

    with col1:
        st.subheader("Cluster 1")
        st.metric("Total Cluster 1", total_cluster1, delta_color="off")
    with col2:
        st.subheader("Cluster 2")
        st.metric("Total Cluster 2", total_cluster2, delta_color="off")
    with col3:
        st.subheader("Cluster 3")
        st.metric("Total Cluster 3", total_cluster3, delta_color="off")
    with col4:
        st.subheader("Cluster 4")
        st.metric("Total Cluster 4", total_cluster4, delta_color="off")
    style_metric_cards(background_color="#0e1117", border_left_color="#ed1d56", border_color="#000000",
                       box_shadow="#F71938")


def display_kmeans_cluster1(df):
    cluster_1_df = df[df['cluster_kmeans'] == 1]
    st.write(cluster_1_df)

    st.subheader("Kesimpulan")
    st.markdown('''
        - Rentang bulan Januari hingga Desember menunjukkan penjualan yang stabil dan dominan oleh tipe mobil Omoda 5 RZ (4x2) AT.
        - Meskipun terdapat variasi bulan ke bulan, tipe mobil ini secara konsisten menjadi pilihan utama konsumen dalam cluster ini.
        - Cluster ini menunjukkan kecenderungan untuk tetap fokus pada satu tipe mobil yang menunjukkan preferensi kuat dari pelanggan.
        ''')

    st.markdown("---")


def display_kmeans_cluster2(df):
    cluster_2_df = df[df['cluster_kmeans'] == 2]
    st.write(cluster_2_df)

    st.subheader("Kesimpulan")
    st.markdown('''
    - Rentang bulan Mei hingga Desember menunjukkan dominasi penjualan oleh tipe mobil Omoda 5 Z(4x2) AT.
    - Kecuali pada bulan Juni, Juli, dan November, di mana tidak ada penjualan untuk tipe mobil ini.
    - Selain itu, terdapat variasi dengan penjualan tipe mobil Tiggo 7 Pro Comfort (4x2) AT pada bulan Mei dan Agustus.
    - Cluster ini menunjukkan kecenderungan untuk beralih antara dua tipe mobil utama, tetapi tetap dengan fokus pada tipe mobil utama, yaitu Omoda 5 Z(4x2) AT.
    ''')

    st.markdown("---")



def display_kmeans_cluster3(df):
    cluster_3_df = df[df['cluster_kmeans'] == 3]
    st.write(cluster_3_df)

    st.subheader("Kesimpulan")
    st.markdown('''
    - Rentang bulan Januari hingga Desember menunjukkan dominasi penjualan oleh tipe mobil Tiggo 7 Pro Premium (4x2) AT Two Tone.
    - Meskipun terdapat bulan-bulan tanpa penjualan, tipe mobil ini tetap menjadi pilihan utama dalam cluster ini.
    - Selain itu, terdapat variasi dengan penjualan tipe mobil Tiggo 7 Pro Luxury (4x2) AT pada bulan Mei, serta Tiggo 7 Pro Premium (4x2) hanya terjual pada bulan Januari, Februari, September, dan Desember.
    - Cluster ini menunjukkan kecenderungan untuk tetap fokus pada satu tipe mobil yang menunjukkan preferensi kuat dari pelanggan, meskipun ada variasi dalam jenis tipe mobil yang terjual.
    ''')

    st.markdown("---")

def display_kmeans_cluster4(df):
    cluster_4_df = df[df['cluster_kmeans'] == 4]
    st.write(cluster_4_df)

    st.subheader("Kesimpulan")
    st.markdown('''
    - Rentang bulan Januari hingga Desember menunjukkan penjualan yang konsisten dengan dominasi oleh tipe mobil Tiggo 8 Pro Premium (4x2) AT.
    - Meskipun terdapat bulan-bulan tanpa penjualan, tipe mobil ini tetap menjadi pilihan utama dalam cluster ini.
    - Cluster ini menunjukkan kestabilan dalam pola penjualan dengan fokus utama pada satu tipe mobil, yaitu Tiggo 8 Pro Premium (4x2) AT.
    ''')

    st.markdown("---")


def clustering_kmeans(df):
    st.subheader("Persebaran Data Setiap Cluster Berdasarkan Bulan SPK dan Tipe Mobil Penjualan")
    data_model = df.drop(['cluster_hc'], axis=1).copy()
    fig = px.scatter(data_model, x='Month_SPK', y='Tipe Mobil', color='cluster_kmeans',
                     color_continuous_scale=px.colors.qualitative.Set1)
    st.plotly_chart(fig, use_container_width=True, style={'border': '1px solid black'})
    st.markdown('''
    Terlihat pada grafik scatter plot di atas terdapat 4 cluster, di mana masing-masing cluster memiliki ciri khas:

- **Cluster 1:** Rentang bulan Januari hingga Desember menunjukkan penjualan mobil yang didominasi oleh tipe **Omoda 5 RZ (4x2) AT**, dengan jumlah penjualan lebih tinggi dibandingkan dengan tipe mobil **Omoda 5 Z (4x2) AT Two Tone** yang hanya terjual pada bulan Maret, April, Agustus, September, Oktober, dan Desember.
- **Cluster 2:** Rentang bulan Mei hingga Desember menunjukkan penjualan yang didominasi oleh tipe mobil **Omoda 5 Z(4x2) AT**, kecuali bulan Juni, Juli, dan November yang tidak memiliki penjualan dengan tipe mobil tersebut. Selain itu, terdapat penjualan dengan tipe mobil **Tiggo 7 Pro Comfort (4x2) AT** pada bulan Mei dan Agustus.
- **Cluster 3:** Rentang bulan Januari hingga Desember menunjukkan penjualan yang didominasi oleh tipe mobil **Tiggo 7 Pro Premium (4x2) AT Two Tone**, walaupun tidak ada penjualan pada bulan April, Mei, Juli, Agustus, Oktober, November, dan Desember. Selain itu, terdapat penjualan dengan tipe mobil **Tiggo 7 Pro Luxury (4x2) AT** hanya pada bulan Mei, serta penjualan dengan tipe mobil **Tiggo 7 Pro Premium (4x2)** yang hanya terjual pada bulan Januari, Februari, September, dan Desember.
- **Cluster 4:** Rentang bulan Januari hingga Desember menunjukkan penjualan yang didominasi oleh satu tipe mobil, yaitu **Tiggo 8 Pro Premium (4x2) AT**, meskipun tidak ada penjualan pada bulan September, November, dan Desember.
    ''')
    st.markdown("---")
    selected_tab = option_menu(
        "Dataframe Setiap Cluster",
        options=["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4"],
        icons=["bar-chart", "bar-chart", "bar-chart", "bar-chart"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "nav": {
                "border-radius": "10px",
            },
            "nav-item": {
                "margin": "0px 5px",
            },
            "icon": {
                "color": "white",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0px 12px",
                "--hover-color": "#a01239",
                "padding": "8px 12px",
                "border-radius": "10px",
            },
            "nav-link-selected": {
                "background-color": "#ed1d56",
                "color": "white",
                "border-radius": "10px",
            },
        }
    )

    if selected_tab == "Cluster 1":
        display_kmeans_cluster1(df)
    elif selected_tab == "Cluster 2":
        display_kmeans_cluster2(df)
    elif selected_tab == "Cluster 3":
        display_kmeans_cluster3(df)
    elif selected_tab == "Cluster 4":
        display_kmeans_cluster4(df)


def main():
    st.title("Clustering")

    with st.expander("Lihat Dataset"):
        dataset(data_modeling)

    display_kmeans(data_modeling)

    st.markdown("---")

    clustering_kmeans(data_modeling)
