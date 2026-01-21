# 🧬 Simulator Sistem Dinamis Penyebaran COVID-19

Simulator ini merupakan aplikasi **sistem dinamis kontinu** yang memodelkan penyebaran COVID-19 menggunakan **Model Epidemiologi SIR (Susceptible–Infected–Recovered)** dengan penyelesaian numerik **Runge-Kutta Orde 4 (RK4)**. Aplikasi dilengkapi dengan **antarmuka web interaktif berbasis Streamlit** sehingga pengguna awam dapat melakukan *What-If Analysis* tanpa perlu memodifikasi kode.

---

## 🎯 Tujuan Proyek

Proyek ini dikembangkan untuk memenuhi tugas jalur **Simulator Sistem Dinamis (Kontinu)** dengan tujuan:

* Memprediksi perilaku sistem penyebaran penyakit menggunakan persamaan diferensial
* Mengimplementasikan metode numerik RK4
* Memvalidasi model menggunakan data time series riil (Kaggle)
* Menyediakan aplikasi interaktif untuk analisis skenario

---

## 🧠 Konsep Dasar

Model SIR membagi populasi menjadi tiga kompartemen:

* **S (Susceptible)** : Individu rentan terhadap penyakit
* **I (Infected)** : Individu terinfeksi (kasus aktif)
* **R (Recovered)** : Individu sembuh atau meninggal

Model ini direpresentasikan dengan sistem persamaan diferensial nonlinier dan diselesaikan menggunakan metode **Runge-Kutta Orde 4**.

---

## 📊 Dataset

Dataset yang digunakan adalah **COVID-19 Time Series Dataset** dari Kaggle, dengan karakteristik:

* Data harian
* Skala global
* Variabel utama: Confirmed, Recovered, Deaths

Pada implementasi ini digunakan studi kasus negara **Germany** karena data yang konsisten dan lengkap.

---

## 🧩 Fitur Utama

✅ Model SIR berbasis sistem dinamis kontinu
✅ Penyelesaian numerik menggunakan RK4
✅ Validasi dengan data riil COVID-19
✅ Visualisasi interaktif (Plotly)
✅ Panel kontrol dengan slider parameter
✅ Tombol **Run Simulation**
✅ Kesimpulan otomatis berbasis hasil simulasi

---

## 🖥️ Struktur Proyek

```text
covid-sir-simulator/
├── app.py                     # Aplikasi Streamlit (UI & simulasi)
├── requirements.txt           # Daftar dependensi
├── README.md                  # Dokumentasi proyek
├── data/
│   └── time-series-19-covid-combined.csv
├── src/
│   ├── data_loader.py         # Load & preprocessing data
│   ├── rk4_solver.py          # Implementasi RK4
│   └── sir_model.py           # Persamaan diferensial SIR
└── notebooks/
    └── 01_sir_rk4_simulation.ipynb
```

---

## ⚙️ Instalasi & Persiapan

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/covid-sir-simulator.git
cd covid-sir-simulator
```

### 2️⃣ Buat Virtual Environment (Disarankan)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependensi

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Notebook (Analisis & Validasi)

Notebook digunakan untuk:

* Load data
* Exploratory Data Analysis (EDA)
* Implementasi model SIR
* Visualisasi hasil simulasi

```bash
jupyter notebook
```

Buka file:

```
notebooks/01_sir_rk4_simulation.ipynb
```

---

## 🌐 Menjalankan Aplikasi Streamlit

Aplikasi web digunakan untuk simulasi interaktif dan *What-If Analysis*.

```bash
streamlit run app.py
```

Akses melalui browser:

```
http://localhost:8501
```

---

## 🎛️ Cara Menggunakan Aplikasi

1. Atur parameter:

   * **β (Laju Infeksi)**
   * **γ (Laju Pemulihan)**
2. Klik tombol **▶ Jalankan Simulasi**
3. Amati:

   * Grafik perbandingan data riil vs model
   * Grafik dinamika S, I, dan R
   * Kesimpulan otomatis simulasi

Aplikasi dirancang agar **pengguna awam** dapat memahami dampak perubahan parameter tanpa menyentuh kode.

---

## 📝 Output Analisis

Aplikasi menghasilkan:

* Grafik time series interaktif
* Indikator puncak kasus
* Analisis tingkat penyebaran
* Kesimpulan berbasis parameter

Hasil ini dapat digunakan untuk:

* Edukasi
* Simulasi kebijakan
* Studi sistem dinamis

---

## 👨‍🎓 Identitas Pengembang

**Nama** : Ardi Kamal Karima
**Kelas** : 5C
**NIM** : 301230023
**Program Studi** : Teknik Informatika
**Universitas** : Universitas Bale Bandung (UNIBBA)

---

## 📚 Referensi

* Kermack, W. O., & McKendrick, A. G. (1927). *A contribution to the mathematical theory of epidemics*.
* World Health Organization (WHO). COVID-19 Pandemic Data.
* Kaggle COVID-19 Time Series Dataset.

---

⭐ Jika proyek ini bermanfaat, silakan beri *star* pada repository ini.
