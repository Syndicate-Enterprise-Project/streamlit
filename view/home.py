import streamlit as st
import pandas as pd
import plotly.express as px
from model import model as data
from streamlit_extras.metric_cards import style_metric_cards

data_clean = data.load_data_clean()
data_modelling = data.load_data_modelling()


def dataset(df):
    filter_options = ['No. Penjualan', 'Tanggal Pengiriman', 'Tanggal Penjualan', 'Tipe Mobil', 'Warna',
                      'Sumber Penjualan', 'No. SPK',
                      'Tahun Pembuatan', 'On/Off The Road', 'Harga (Rp)', 'Cara Pembayaran']
    selected_filters = st.multiselect("Pilih kolom untuk filter:", filter_options)

    if selected_filters:
        filtered_df = df.loc[:, selected_filters]
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)


def top_analytics(df):
    total_penjualan = df['Harga (Rp)'].sum()
    rata_rata_penjualan = df['Harga (Rp)'].mean()
    median_penjualan = df['Harga (Rp)'].median()

    analytics1, analytics2, analytics3 = st.columns(3)

    with analytics1:
        st.info('Total Penjualan', icon="💰")
        st.metric("Total Penjualan", f"Rp {total_penjualan:,}")

    with analytics2:
        st.info('Rata-Rata Penjualan', icon="💰")
        st.metric("Rata-rata Penjualan", f"Rp {rata_rata_penjualan:,}")

    with analytics3:
        st.info('Median Penjualan', icon="💰")
        st.metric("Median Penjualan", f"Rp {median_penjualan:,}")
    style_metric_cards(background_color="#0e1117", border_left_color="#686664", border_color="#000000",
                       box_shadow="#F71938")


def graph_tab1(df):
    st.caption("Diagram Line Chart Penjualan Chery per Bulan (2023)")

    df['Tanggal SPK'] = pd.to_datetime(df['Tanggal SPK'])

    total_penjualan_per_bulan = df.groupby(df['Tanggal SPK'].dt.strftime('%B')).size().reset_index(
        name='Jumlah Penjualan')
    bulan_urutan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']
    total_penjualan_per_bulan['Bulan'] = pd.Categorical(total_penjualan_per_bulan['Tanggal SPK'],
                                                        categories=bulan_urutan, ordered=True)
    total_penjualan_per_bulan = total_penjualan_per_bulan.sort_values('Bulan')

    fig_line = px.line(total_penjualan_per_bulan, x='Bulan', y='Jumlah Penjualan',
                       title='Jumlah Penjualan Mobil Chery per Bulan (2023)')
    fig_line.update_xaxes(title='Bulan')
    fig_line.update_yaxes(title='Jumlah Penjualan')
    fig_line.update_layout(title_x=0.5)
    st.plotly_chart(fig_line, use_container_width=True, style={'border': '1px solid black'})

    st.caption("Diagram Bar Chart Penjualan Berdasarkan Sumber Penjualan, Tipe Mobil, dan Warna Mobil (2023)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Sumber Penjualan")
        jumlah_penjualan_per_sumber = df['Sumber Penjualan'].value_counts().reset_index()
        jumlah_penjualan_per_sumber.columns = ['Sumber Penjualan', 'Jumlah Penjualan']
        fig_sumber = px.bar(jumlah_penjualan_per_sumber, y='Sumber Penjualan', x='Jumlah Penjualan',
                            orientation='h', title='Jumlah Penjualan Mobil Chery berdasarkan Sumber Penjualan',
                            category_orders={'Sumber Penjualan': jumlah_penjualan_per_sumber.sort_values(
                                'Jumlah Penjualan')['Sumber Penjualan']})
        fig_sumber.update_xaxes(title='Jumlah Penjualan')
        fig_sumber.update_yaxes(title='Sumber Penjualan')
        st.plotly_chart(fig_sumber, use_container_width=True, style={'border': '1px solid black'})

    with col2:
        # Diagram Bar Chart Penjualan Berdasarkan Tipe Mobil
        st.subheader("Tipe Mobil")
        jumlah_penjualan_per_tipemobil = df['Tipe Mobil'].value_counts().reset_index()
        jumlah_penjualan_per_tipemobil.columns = ['Tipe Mobil', 'Jumlah Penjualan']
        fig_tipemobil = px.bar(jumlah_penjualan_per_tipemobil, y='Tipe Mobil', x='Jumlah Penjualan',
                               orientation='h', title='Jumlah Penjualan Mobil Chery berdasarkan Tipe Mobil',
                               category_orders={'Tipe Mobil': jumlah_penjualan_per_tipemobil.sort_values(
                                   'Jumlah Penjualan')['Tipe Mobil']})
        fig_tipemobil.update_xaxes(title='Jumlah Penjualan')
        fig_tipemobil.update_yaxes(title='Tipe Mobil')
        st.plotly_chart(fig_tipemobil, use_container_width=True, style={'border': '1px solid black'})

    with col3:
        # Diagram Bar Chart Penjualan Berdasarkan Warna Mobil
        st.subheader("Warna Mobil")
        jumlah_penjualan_per_warna = df['Warna'].value_counts().reset_index()
        jumlah_penjualan_per_warna.columns = ['Warna Mobil', 'Jumlah Penjualan']
        fig_warna = px.bar(jumlah_penjualan_per_warna, y='Warna Mobil', x='Jumlah Penjualan',
                           orientation='h', title='Jumlah Penjualan Mobil Chery berdasarkan Warna Mobil',
                           category_orders={'Warna Mobil': jumlah_penjualan_per_warna.sort_values(
                               'Jumlah Penjualan')['Warna Mobil']})
        fig_warna.update_xaxes(title='Jumlah Penjualan')
        fig_warna.update_yaxes(title='Warna Mobil')
        st.plotly_chart(fig_warna, use_container_width=True, style={'border': '1px solid black'})


def graph_tab2(df):
    df['Tanggal SPK'] = pd.to_datetime(df['Tanggal SPK'])
    df['Tanggal Penjualan'] = pd.to_datetime(df['Tanggal Penjualan'])
    df['Tanggal Pengiriman'] = pd.to_datetime(df['Tanggal Pengiriman'])

    fig = px.scatter(df, x='Tanggal Penjualan', y='Tanggal SPK', title='Scatter Plot Tanggal Penjualan dan Tanggal SPK')
    fig.update_layout(xaxis_title='Tanggal Penjualan', yaxis_title='Tanggal SPK', xaxis_tickangle=0)
    st.plotly_chart(fig, use_container_width=True, style={'border': '1px solid black'})


def graph_tab3(df):
    payment = df['Cara Pembayaran'].value_counts()
    fig = px.pie(names=payment.index, values=payment.values, title="Jenis Pembayaran Mobil di Dealer Chery")
    fig.update_traces(marker=dict(colors=['#6B5B95', '#FF6F61'], line=dict(color='#FFFFFF', width=2)))
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig, use_container_width=True, style={'border': '1px solid black'})


def graph_tab4(df):
    df['Tanggal SPK'] = pd.to_datetime(df['Tanggal SPK'])

    total_penjualan_per_bulan = df.groupby(df['Tanggal SPK'].dt.strftime('%B')).size().reset_index(
        name='Jumlah Penjualan')
    bulan_urutan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']
    total_penjualan_per_bulan['Bulan'] = pd.Categorical(total_penjualan_per_bulan['Tanggal SPK'],
                                                        categories=bulan_urutan, ordered=True)
    total_penjualan_per_bulan = total_penjualan_per_bulan.sort_values('Bulan')

    fig = px.bar(total_penjualan_per_bulan, x='Bulan', y='Jumlah Penjualan', color='Bulan',
                 labels={'Jumlah Penjualan': 'Jumlah Penjualan Mobil', 'Bulan': 'Bulan'})
    fig.update_layout(title='Jumlah Penjualan Mobil Chery per Bulan (2023)', xaxis_title='Bulan',
                      yaxis_title='Jumlah Penjualan')
    st.plotly_chart(fig, use_container_width=True, style={'border': '1px solid black'})


def main():
    st.title("Dashboard Penjualan Chery (2023)!")

    with st.expander("Lihat Dataset"):
        dataset(data_clean)

    top_analytics(data_clean)

    tab1, tab2, tab3, tab4 = st.tabs(["Comparison", "Relation", "Composition", "Distribution"])

    with tab1:
        graph_tab1(data_clean)

    with tab2:
        graph_tab2(data_clean)

    with tab3:
        graph_tab3(data_clean)

    with tab4:
        graph_tab4(data_clean)


if __name__ == "__main__":
    main()
