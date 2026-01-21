import streamlit as st
import plotly.graph_objects as go
import numpy as np

from src.data_loader import load_covid_data
from src.rk4_solver import rk4_sir

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="Simulator Sistem Dinamis COVID-19",
    page_icon="🧬",
    layout="wide"
)

# =============================
# HEADER
# =============================
st.markdown("""
<h1 style='text-align:center;'>🧬 Simulator Sistem Dinamis COVID-19</h1>
<p style='text-align:center; color:gray;'>
Model Epidemiologi SIR (Kontinu) menggunakan Metode Runge-Kutta Orde 4
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# =============================
# SIDEBAR – PANEL KONTROL
# =============================
st.sidebar.markdown("## 🎛️ Panel Kontrol Simulasi")

st.sidebar.info(
    """
    **Petunjuk Penggunaan**
    
    1. Atur parameter simulasi  
    2. Klik **Jalankan Simulasi**  
    3. Amati grafik dan kesimpulan
    """
)

with st.sidebar.form("simulation_form"):
    beta = st.slider(
        "🦠 Laju Infeksi (β)",
        0.05, 0.8, 0.3, 0.01,
        help="Semakin besar β → Penyakit menyebar lebih cepat"
    )

    gamma = st.slider(
        "💊 Laju Pemulihan (γ)",
        0.01, 0.5, 0.1, 0.01,
        help="Semakin besar γ → Pasien sembuh lebih cepat"
    )

    run_button = st.form_submit_button("▶ Jalankan Simulasi")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📌 Contoh Skenario
- **β tinggi, γ rendah** → Lonjakan kasus
- **β rendah, γ tinggi** → Wabah terkendali
""")

st.sidebar.markdown("""
### 📖 Keterangan Model
- **S** : Rentan  
- **I** : Terinfeksi  
- **R** : Sembuh / Meninggal
""")

# =============================
# LOAD DATA
# =============================
df = load_covid_data(
    "data/time-series-19-covid-combined.csv",
    country="Germany"
)

# =============================
# JALANKAN SIMULASI
# =============================
if run_button:

    # ---- Kondisi Awal ----
    N = 83_000_000
    I0 = max(df["Active"].iloc[0], 1)
    R0 = df["Recovered"].iloc[0]
    S0 = N - I0 - R0

    # ---- Simulasi RK4 ----
    S, I, R = rk4_sir(beta, gamma, S0, I0, R0, len(df))

    df["S_Model"] = S
    df["I_Model"] = I
    df["R_Model"] = R

    # =============================
    # METRIC RINGKASAN
    # =============================
    col1, col2, col3 = st.columns(3)
    col1.metric("📈 Puncak Kasus (Model)", f"{int(max(I)):,}")
    col2.metric("📉 Kasus Aktif Terakhir", f"{int(I[-1]):,}")
    col3.metric("⚖️ Rasio β / γ", f"{beta/gamma:.2f}")

    st.markdown("---")

    # =============================
    # GRAFIK PERBANDINGAN
    # =============================
    st.subheader("📊 Perbandingan Data Riil vs Model SIR")

    fig_compare = go.Figure()
    fig_compare.add_trace(go.Scatter(
        x=df["Date"], y=df["Active"],
        name="Data Riil", line=dict(width=3)
    ))
    fig_compare.add_trace(go.Scatter(
        x=df["Date"], y=df["I_Model"],
        name="Model SIR (RK4)", line=dict(dash="dash", width=3)
    ))

    fig_compare.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="Jumlah Kasus Aktif",
        template="plotly_white"
    )

    st.plotly_chart(fig_compare, use_container_width=True)

    # =============================
    # GRAFIK DINAMIKA SIR
    # =============================
    st.subheader("📈 Dinamika Kompartemen SIR")

    fig_sir = go.Figure()
    fig_sir.add_trace(go.Scatter(x=df["Date"], y=df["S_Model"], name="S (Rentan)"))
    fig_sir.add_trace(go.Scatter(x=df["Date"], y=df["I_Model"], name="I (Terinfeksi)"))
    fig_sir.add_trace(go.Scatter(x=df["Date"], y=df["R_Model"], name="R (Recovered)"))

    fig_sir.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="Jumlah Populasi",
        template="plotly_white"
    )

    st.plotly_chart(fig_sir, use_container_width=True)

    # =============================
    # ANALISIS & KESIMPULAN
    # =============================
    peak_value = int(max(I))
    peak_day = int(np.argmax(I))
    peak_date = df["Date"].iloc[peak_day]
    final_cases = int(I[-1])
    real_peak = int(df["Active"].max())

    severity_ratio = peak_value / real_peak if real_peak > 0 else 0

    if beta / gamma > 1.5:
        spread_level = "sangat agresif"
    elif beta / gamma > 1.0:
        spread_level = "cukup agresif"
    else:
        spread_level = "terkendali"

    if severity_ratio > 1.2:
        severity_text = "lebih buruk dibandingkan data riil"
    elif severity_ratio < 0.8:
        severity_text = "lebih terkendali dibandingkan data riil"
    else:
        severity_text = "relatif mirip dengan data riil"

    st.markdown("---")
    st.subheader("📝 Kesimpulan Simulasi")

    st.markdown(f"""
    Berdasarkan parameter yang dipilih:

    - Laju penyebaran penyakit tergolong **{spread_level}**
    - Puncak kasus simulasi mencapai **{peak_value:,} kasus**
    - Puncak terjadi sekitar **{peak_date.date()}**
    - Dibandingkan data riil, kondisi simulasi **{severity_text}**
    - Kasus aktif di akhir simulasi sekitar **{final_cases:,} kasus**

    **Interpretasi Umum:**  
    Parameter β dan γ sangat memengaruhi dinamika wabah. Rasio β/γ yang tinggi
    menyebabkan lonjakan kasus yang lebih besar dan durasi wabah yang lebih panjang.
    """)

    st.success("Simulasi berhasil dijalankan. Silakan ubah parameter untuk skenario lain.")

else:
    st.info(
        "👈 Atur parameter di panel kiri lalu klik **Jalankan Simulasi** untuk memulai."
    )

# =============================
# FOOTER IDENTITAS
# =============================
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:gray; font-size:14px;'>
<strong>Dibuat oleh:</strong><br>
Ardi Kamal Karima<br>
Kelas 5C – NIM 301230023<br>
Mahasiswa Teknik Informatika<br>
Universitas Bale Bandung (UNIBBA)
</div>
""", unsafe_allow_html=True)
