# Olist Ecommerce Analysis 📊

## 📝 Deskripsi

Project ini merupakan analisis mendalam terhadap data ecommerce Olist Brasil untuk mengekstrak insight bisnis yang berharga. Analisis ini mencakup berbagai aspek seperti revenue trends, customer satisfaction, geographical distribution, dan pola pembelian customer.

**Tujuan Utama:**
- Menganalisis total revenue dan tren pertumbuhan bulanan
- Mengevaluasi tingkat kepuasan customer berdasarkan rating dan review
- Memahami distribusi geografis customer di Brasil
- Mengidentifikasi produk dan kategori terlaris
- Memberikan rekomendasi strategis untuk pengembangan bisnis

## 🌐 Live Demo

**Dashboard Streamlit:** [https://rizqiecommerceolistdashboard.streamlit.app/](https://rizqiecommerceolistdashboard.streamlit.app/)

## 📊 Dataset

Data yang digunakan dalam project ini berasal dari Kaggle - Brazilian E-Commerce Public Dataset by Olist.

**Sumber Data:** [Kaggle - Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Alternative Link:** [Google Drive](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view?usp=sharing)

Dataset ini berisi informasi real ecommerce transaction dari September 2016 hingga Oktober 2018 yang dibuat oleh Olist Store di marketplace Brasil.

## 🗂️ Struktur Project

```
olist-ecommerce-analysis/
├── dashboard/
│   └── dashboard.py          # Streamlit dashboard aplikasi
├── data/                     # Folder berisi dataset CSV
├── venv/                     # Virtual environment
├── README.md                 # Dokumentasi project
├── requirements.txt          # Dependencies Python
├── rizqinotebook (6).ipynb   # Jupyter notebook untuk analisis
└── url.txt                   # File URL tambahan
```

## 🛠️ Setup Environment

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. **Clone atau download project ini**
```bash
git clone <repository-url>
cd olist-ecommerce-analysis
```

2. **Buat virtual environment**
```bash
python -m venv venv
```

3. **Aktivasi virtual environment**

**Windows:**
```bash
.\venv\Scripts\activate
```

**MacOS/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Menjalankan Aplikasi

### Dashboard Streamlit
```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`

### Jupyter Notebook
```bash
jupyter notebook rizqinotebook\ \(6\).ipynb
```

## 📈 Fitur Dashboard

Dashboard interaktif ini menyediakan visualisasi comprehensive dengan fitur-fitur berikut:

### 🎯 **Main Metrics & Trends**
- **Total Revenue Keseluruhan:** 16,188,779.23 (mata uang Brasil Real)
- **Tren Revenue Bulanan:** Grafik line chart menampilkan perkembangan revenue dari 2016-2018
- **Filter Data:** Pilihan tahun untuk menyaring data berdasarkan periode tertentu

### 🏆 **Geographic & Customer Analysis**
- **Top 7 State dengan Pesanan Terbanyak:** 
  - Visualisasi bar chart menampilkan distribusi pesanan per state
  - São Paulo (SP) mendominasi dengan 48,816 pesanan
- **Distribusi Review Score:** 
  - Histogram menampilkan kepuasan customer (rata-rata: 4.02)
  - Mayoritas customer memberikan rating 5.0 (66,343 reviews)

### 🎖️ **RFM Analysis (Recency, Frequency, Monetary)**
- **Customer Segmentation:** Analisis customers terbaik berdasarkan:
  - **Recency:** Seberapa baru customer melakukan pembelian
  - **Frequency:** Seberapa sering customer berbelanja  
  - **Monetary:** Seberapa besar nilai pembelian customer
- **Customer ID Tracking:** Identifikasi customer dengan performa terbaik

### 📦 **Product & Pricing Analysis**
- **Distribusi Kategori Barang:** 
  - Bar chart menampilkan kategori berdasarkan harga (Sedang, Mahal, Murah)
  - Barang harga sedang mendominasi (54,805 items)
- **Proporsi Price vs Freight Value:**
  - Pie chart menunjukkan komposisi revenue (85.7% dari harga produk, 14.3% ongkos kirim)

### 🗺️ **Geospatial Visualization**
- **Peta Distribusi Global:** Interactive map menampilkan sebaran customer di Brasil
- **Heat Map:** Konsentrasi customer dengan density tinggi di region tertentu
- **Basemap Integration:** Menggunakan OpenStreetMap untuk konteks geografis

### 🔧 **Interactive Features**
- **Filter by Year:** Dropdown untuk memfilter data berdasarkan tahun
- **Responsive Design:** Dashboard yang dapat diakses di berbagai device
- **Real-time Updates:** Data yang terupdate sesuai filter yang dipilih

## 🎯 Metodologi Analisis

### 1. **Data Exploration & Cleaning**
- **Pemahaman struktur data:** Analisis skema database dan relasi antar tabel Olist
- **Data quality assessment:** Identifikasi missing values, duplicates, dan outliers
- **Data preprocessing:** Cleaning dan transformasi data untuk analisis
- **Time series preparation:** Formatting date columns untuk analisis temporal

### 2. **Exploratory Data Analysis (EDA)**
- **Revenue Analysis:** Kalkulasi total revenue dan tren bulanan (2016-2018)
- **Geographic Analysis:** Mapping customer distribution across Brazilian states
- **Customer Satisfaction:** Analisis review scores dan rating distribution
- **Product Categorization:** Segmentasi produk berdasarkan price ranges

### 3. **Advanced Analytics**
- **RFM Analysis:** Customer segmentation berdasarkan Recency, Frequency, Monetary
- **Geospatial Visualization:** Interactive mapping dengan coordinate-based analysis
- **Price-Freight Analysis:** Proporsi analysis untuk logistics optimization
- **Time Series Analysis:** Seasonal pattern identification dan trend analysis

### 4. **Business Intelligence & Visualization**
- **Interactive Dashboard:** Streamlit-based dashboard dengan filtering capabilities
- **KPI Monitoring:** Key metrics tracking (Total Revenue: R$ 16,188,779.23)
- **Geographic Insights:** State-wise performance analysis (SP dominance: 48,816 orders)
- **Customer Insights:** Satisfaction metrics (Average rating: 4.02/5.0)

## 📊 Key Insights

Berdasarkan analisis yang telah dilakukan melalui dashboard, beberapa insight utama yang ditemukan:

### 💰 **Revenue Performance**
- **Total Revenue:** R$ 16,188,779.23 menunjukkan performa bisnis yang solid
- **Tren Pertumbuhan:** Revenue mengalami pertumbuhan signifikan dari 2016-2018
- **Peak Performance:** Puncak revenue terjadi pada pertengahan 2018 (sekitar 1.4M per bulan)
- **Seasonal Pattern:** Terdapat fluktuasi musiman dengan penurunan di akhir periode

### 🌍 **Geographic Distribution**
- **Dominasi São Paulo:** SP state mendominasi dengan 48,816 pesanan (41.7% total)
- **Top 7 States:** SP, RJ, MG, RS, PR, SC, BA berkontribusi mayoritas revenue
- **Konsentrasi Regional:** Customer terkonsentrasi di region Tenggara dan Selatan Brasil
- **Peluang Ekspansi:** Region Utara dan Timur Laut masih memiliki potensi besar

### ⭐ **Customer Satisfaction**
- **Rating Tinggi:** Rata-rata review score 4.02/5.0 menunjukkan kepuasan tinggi
- **Distribusi Positif:** 66,343 customer (mayoritas) memberikan rating 5.0
- **Low Complaint Rate:** Hanya 4,162 customer memberikan rating 2.0
- **Customer Loyalty:** High satisfaction rate mengindikasikan potensi repeat purchase

### 🛍️ **Product & Pricing Strategy**
- **Price Segmentation:** Produk harga sedang dominan (54,805 items)
- **Balanced Portfolio:** Distribusi yang seimbang antara harga murah, sedang, dan mahal
- **Logistics Efficiency:** Freight value hanya 14.3% dari total revenue
- **Competitive Pricing:** Proporsi 85.7% product price menunjukkan value yang baik

### 👥 **Customer Behavior (RFM Analysis)**
- **Recent Activity:** Mayoritas customer masih aktif (recency analysis)
- **Purchase Frequency:** Identifikasi customer dengan frekuensi pembelian tinggi
- **High-Value Customers:** Segmentasi customer berdasarkan monetary value
- **Retention Opportunity:** Customer ID tracking memungkinkan targeted marketing

## 🔧 Dependencies

Berikut adalah libraries utama yang digunakan:

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.6.0
seaborn>=0.12.0
plotly>=5.15.0
folium>=0.14.0
streamlit-folium>=0.13.0
```

Lihat `requirements.txt` untuk daftar lengkap dependencies.

## 📝 Cara Kontribusi

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/improvement`)
3. Commit perubahan (`git commit -am 'Add new feature'`)
4. Push ke branch (`git push origin feature/improvement`)
5. Buat Pull Request

## 📄 License

Project ini menggunakan lisensi yang sama dengan dataset asli dari Olist. Silakan merujuk ke [Kaggle dataset page](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) untuk informasi lisensi.

## 👤 Author

**Rizqi Maulidi**
- GitHub: [@rizqi-maulidi](https://github.com/rizqi-maulidi)
- Dashboard: [Streamlit App](https://rizqiecommerceolistdashboard.streamlit.app/)

## 🙏 Acknowledgments

- **Olist** untuk menyediakan dataset yang sangat berharga
- **Kaggle** sebagai platform untuk berbagi dataset
- **Streamlit** untuk framework dashboard yang mudah digunakan
- **Python community** untuk tools dan libraries yang luar biasa

---

⭐ Jika project ini bermanfaat, jangan lupa berikan star di repository ini!
