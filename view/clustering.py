import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from model import model as data
from streamlit_extras.metric_cards import style_metric_cards

data_modeling = data.load_data_modelling()
data_clean = data.load_data_clean()

def dataset(df):
    filter_options = ['cluster_kmeans', 'cluster_hc', 'Tipe Mobil', 'Warna', 'Sumber Penjualan', 'Harga (Rp)',
                      'Cara Pembayaran']
    selected_filters = st.multiselect("Pilih kolom untuk filter:", filter_options)

    if selected_filters:
        filtered_df = df.loc[:, selected_filters]
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

    cluster1 = df[df['cluster_kmeans'] == 0]
    total_cluster1 = cluster1['cluster_kmeans'].count()

    cluster2 = df[df['cluster_kmeans'] == 1]
    total_cluster2 = cluster2['cluster_kmeans'].count()

    cluster3 = df[df['cluster_kmeans'] == 2]
    total_cluster3 = cluster3['cluster_kmeans'].count()

    cluster4 = df[df['cluster_kmeans'] == 3]
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

def display_hc(df):
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

    cluster1 = df[df['cluster_hc'] == 0]
    total_cluster1 = cluster1['cluster_hc'].count()

    cluster2 = df[df['cluster_hc'] == 1]
    total_cluster2 = cluster2['cluster_hc'].count()

    cluster3 = df[df['cluster_hc'] == 2]
    total_cluster3 = cluster3['cluster_hc'].count()

    cluster4 = df[df['cluster_hc'] == 3]
    total_cluster4 = cluster4['cluster_hc'].count()

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

def clustering_kmeans(df):
    data_model = df.drop(['cluster_hc'], axis=1).copy()
    fig = px.scatter(data_model, x='Month_SPK', y='Tipe Mobil', color='cluster_kmeans',
                     color_continuous_scale=px.colors.qualitative.Set1)
    st.plotly_chart(fig, use_container_width=True, style={'border': '1px solid black'})


def main():
    st.title("Clustering")

    with st.expander("Lihat Dataset"):
        dataset(data_modeling)

    select_algorithm = st.selectbox("Pilih Algoritma Clustering", ["Pilih Algoritma", "K-Means", "Hierarchical"])

    if select_algorithm == "Pilih Algoritma":
        st.warning("Silahkan pilih algoritma terlebih dahulu")
    elif select_algorithm == "K-Means":
        display_kmeans(data_modeling)
    elif select_algorithm == "Hierarchical":
        display_hc(data_modeling)

    st.markdown("---")

    if select_algorithm == "K-Means":
        clustering_kmeans(data_modeling)






