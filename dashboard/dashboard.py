import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
import geopandas as gpd
import contextily as ctx  # Untuk menambahkan basemap
import numpy as np

# Load dataset
final_orders = pd.read_csv("C:/Users/Rizqi Maulidi/proyek_analisis_data/dashboard/final_orders_df.csv")

# Konversi kolom tanggal ke datetime
final_orders["order_delivered_customer_date"] = pd.to_datetime(final_orders["order_delivered_customer_date"])

# Streamlit Dashboard
st.title("📊 E-Commerce Sales Dashboard")

#Kasih gambar biar cakep
st.sidebar.image("https://img.freepik.com/premium-vector/free-vector-dark-blue-orange-online-shop-logo_883906-585.jpg")

# Sidebar Filter
st.sidebar.header("Filter Data")

# Menambahkan opsi "Semua Tahun"
years = final_orders["order_delivered_customer_date"].dt.year.unique().tolist()
years.sort()
years.insert(0, "Semua Tahun")

selected_year = st.sidebar.selectbox("Pilih Tahun", years)

st.sidebar.write("🔍 Gunakan filter diatas untuk menyaring data berdasarkan kebutuhan Anda.")

# Filter berdasarkan tahun yang dipilih
if selected_year != "Semua Tahun":
    filtered_orders = final_orders[final_orders["order_delivered_customer_date"].dt.year == selected_year]
else:
    filtered_orders = final_orders.copy()  # Menampilkan semua tahun

# Filter hanya pesanan dengan status 'delivered'
delivered_orders = filtered_orders[filtered_orders["order_status"] == "delivered"]

st.subheader("💰 Total Revenue Keseluruhan : 16,188,779.23")

# VISUALISASI revnue per Month
st.subheader("📈 Tren Total Revenue Setiap Bulan")
monthly_revenue = (
    delivered_orders
    .groupby(delivered_orders["order_delivered_customer_date"].dt.to_period("M"))
    .agg(total_revenue=("price", "sum"), total_freight=("freight_value", "sum"))
)

# Menambahkan total revenue
monthly_revenue["total_revenue"] = monthly_revenue["total_revenue"] + monthly_revenue["total_freight"]
monthly_revenue = monthly_revenue.reset_index()
monthly_revenue["order_delivered_customer_date"] = monthly_revenue["order_delivered_customer_date"].astype(str)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    monthly_revenue["order_delivered_customer_date"],
    monthly_revenue["total_revenue"],
    marker="o",
    linewidth=2,
    color="#72BCD4"
)
ax.set_title("Total Revenue per Month", fontsize=14)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Total Revenue", fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig)

col1, col2 = st.columns(2)  # Membuat dua kolom

with col1:
    st.subheader("🏆Top 7 State dengan Pesanan Terbanyak")
    top_7_states = delivered_orders["customer_state"].value_counts().nlargest(7)

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.barplot(x=top_7_states.index, y=top_7_states.values, palette="viridis", ax=ax1)

    for i, value in enumerate(top_7_states.values):
        ax1.text(i, value + (value * 0.02), str(value), ha="center", fontsize=10, fontweight="bold")

    ax1.set_title("Top 7 State dengan Pesanan Terbanyak", fontsize=12)
    ax1.set_xlabel("State (customer_state)", fontsize=10)
    ax1.set_ylabel("Jumlah Pesanan", fontsize=10)
    plt.xticks(rotation=45)

    st.pyplot(fig1)

with col2:
    st.subheader("⭐ Distribusi Review Score")
    valid_reviews = filtered_orders.dropna(subset=["review_score"])

    if not valid_reviews.empty:
        review_counts = valid_reviews["review_score"].value_counts().sort_index()
        avg_review_score = valid_reviews["review_score"].mean()

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.barplot(x=review_counts.index, y=review_counts.values, palette="viridis", ax=ax2)

        for i, v in enumerate(review_counts.values):
            ax2.text(i, v + 5, str(v), ha='center', fontsize=10)

        ax2.axhline(y=avg_review_score, color='red', linestyle='dashed', linewidth=2, label=f'Rata-rata: {avg_review_score:.2f}')
        ax2.set_title("Distribusi Review Score", fontsize=12)
        ax2.set_xlabel("Review Score", fontsize=10)
        ax2.set_ylabel("Jumlah Review", fontsize=10)
        ax2.legend()

        st.pyplot(fig2)
    else:
        st.warning("Tidak ada data review score untuk tahun yang dipilih.")

# RFM Analysis visualisasi
st.subheader("🏅 Customers Terbaik Berdasarkan RFM Analisis")

# Kelompokkan data berdasarkan customer_id dan hitung nilai RFM
rfm_df = delivered_orders.groupby(by="customer_id", as_index=False).agg({
    "order_delivered_customer_date": "max",
    "order_id": "nunique",
    "price": "sum",
    "freight_value": "sum"
})

rfm_df["monetary"] = rfm_df["price"] + rfm_df["freight_value"]
rfm_df.rename(columns={"order_delivered_customer_date": "max_order_timestamp", "order_id": "frequency"}, inplace=True)

# Cari tanggal terbaru dalam dataset
recent_date = delivered_orders["order_delivered_customer_date"].max().date()
rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date

# Menghitung nilai Recency
rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)

rfm_df.drop(["max_order_timestamp", "price", "freight_value"], axis=1, inplace=True)
rfm_df["short_customer_id"] = rfm_df["customer_id"].str[:5]

# Membuat subplot dengan 3 grafik
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(36, 10))
plt.subplots_adjust(wspace=0.5)

colors = ["#72BCD4"] * 5

# Recency
sns.barplot(x="recency", y="short_customer_id",
            data=rfm_df.sort_values(by="recency", ascending=True).head(5),
            palette=colors, ax=ax[0])
ax[0].set_ylabel("Customer ID", fontsize=23)
ax[0].set_xlabel("Recency (days)", fontsize=23)
ax[0].set_title("By Recency (days)", loc="center", fontsize=27)
ax[0].tick_params(axis='y', labelsize=23)

# Frequency
sns.barplot(x="frequency", y="short_customer_id",
            data=rfm_df.sort_values(by="frequency", ascending=False).head(5),
            palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Frequency", fontsize=23)
ax[1].set_title("By Frequency", loc="center", fontsize=27)
ax[1].tick_params(axis='y', labelsize=23)

# Monetary
sns.barplot(x="monetary", y="short_customer_id",
            data=rfm_df.sort_values(by="monetary", ascending=False).head(5),
            palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel("Monetary", fontsize=23)
ax[2].set_title("By Monetary", loc="center", fontsize=27)
ax[2].tick_params(axis='y', labelsize=23)

plt.suptitle("Best Customers Based on RFM Parameters (customer_id)", fontsize=24, y=1.05)
plt.tight_layout(pad=5)
st.pyplot(fig)

col1, col2 = st.columns(2)  # Membuat dua kolom berdampingan

with col1:
    st.subheader("📦 Distribusi Kategori Barang Berdasarkan Harga")
    
    valid_prices = filtered_orders.dropna(subset=["price"])

    if not valid_prices.empty:
        q1 = valid_prices["price"].quantile(0.25)
        q3 = valid_prices["price"].quantile(0.75)
        mean_price = valid_prices["price"].mean()

        def categorize_price(price):
            if price <= q1:
                return "Barang Harga Murah"
            elif price <= mean_price:
                return "Barang Harga Sedang"
            else:
                return "Barang Harga Mahal"

        valid_prices["price_category"] = valid_prices["price"].apply(categorize_price)
        category_counts = valid_prices["price_category"].value_counts()

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.barplot(x=category_counts.index, y=category_counts.values, palette=["blue", "orange", "red"], ax=ax1)

        max_count = category_counts.max()
        offset = max(10, max_count * 0.02)

        for i, count in enumerate(category_counts.values):
            ax1.text(i, count + offset, str(count), ha='center', fontsize=10, fontweight='bold')

        ax1.set_xlabel("Kategori Barang", fontsize=10)
        ax1.set_ylabel("Jumlah Barang", fontsize=10)
        ax1.set_title("Distribusi Kategori Barang", fontsize=12)

        st.pyplot(fig1)

    else:
        st.warning("Tidak ada data harga barang untuk tahun yang dipilih.")

with col2:
    st.subheader("💵 Proporsi Price vs Freight Value dalam Total Revenue")

    if 'final_orders' in globals():
        delivered_orders = final_orders[final_orders['order_status'] == 'delivered']

        if not delivered_orders.empty:
            total_revenue = delivered_orders['price'].sum() + delivered_orders['freight_value'].sum()
            net_profit = total_revenue

            labels = ["Price", "Freight Value"]
            values = [delivered_orders["price"].sum(), delivered_orders["freight_value"].sum()]
            colors = ["#4CAF50", "#FF9800"]

            fig2, ax2 = plt.subplots(figsize=(6, 4))
            ax2.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, 
                    wedgeprops={"edgecolor": "white"}, textprops={"fontsize": 10})

            plt.title("Proporsi Revenue", fontsize=12)

            st.pyplot(fig2)
        else:
            st.warning("Tidak ada data pesanan dengan status 'delivered'.")
    else:
        st.error("Dataframe 'final_orders_df' tidak ditemukan.")


# Peta Geospasial

geolocation_dataset_df = pd.read_csv("C:/Users/Rizqi Maulidi/proyek_analisis_data/dashboard/geolocation_dataset.csv")

st.subheader("🗺️ Geospatial Distribution with Basemap")

# Pastikan 'geolocation_dataset_df' tersedia
if 'geolocation_dataset_df' in globals():
    # Membuat GeoDataFrame dari dataset
    gdf = gpd.GeoDataFrame(
        geolocation_dataset_df,
        geometry=gpd.points_from_xy(
            geolocation_dataset_df["geolocation_lng"], 
            geolocation_dataset_df["geolocation_lat"]
        ),
        crs="EPSG:4326"  # Koordinat awal dalam WGS 84
    )

    gdf = gdf.to_crs(epsg=3857)

    # Membuat plot dengan basemap
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, markersize=1, alpha=0.5, color="red")  # Titik lokasi
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)  # Tambahkan peta

    # Menambahkan judul
    plt.title("Geospatial Distribution with Basemap", fontsize=14)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
else:
    st.error("Dataframe 'geolocation_dataset_df' tidak ditemukan.")







