import streamlit as st
import pandas as pd
import pickle
import os

# 1. Konfigurasi Halaman Web
st.set_page_config(page_title="Smart Retention Dashboard", page_icon="💸", layout="wide")

st.title("💸 Smart Retention: Cost-Benefit Analysis Dashboard")
st.write("Dashboard ini mensimulasikan dampak finansial dari penggunaan model Machine Learning untuk mencegah Customer Churn.")

# 2. Memuat Model dan Data yang sudah kita simpan
@st.cache_resource
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, '../notebooks/churn_model_data.pkl')
    with open(MODEL_PATH, 'rb') as file:
        return pickle.load(file)

data = load_data()
model = data['model']
X_test = data['X_test']
y_test = data['y_test']

# 3. AI Melakukan Prediksi
predictions = model.predict(X_test)
hasil_df = X_test.copy()
hasil_df['Actual_Churn'] = y_test
hasil_df['Predicted_Churn'] = predictions

# 4. Membuat Kalkulator Interaktif di Sidebar (Menu Samping)
st.sidebar.header("⚙️ Skenario Strategi Retensi")
st.sidebar.write("Sesuaikan parameter di bawah untuk simulasi:")

# Slider interaktif untuk HRD/User
biaya_promo = st.sidebar.slider("Biaya Promo Per Pelanggan ($)", min_value=5, max_value=50, value=20, step=5)
tingkat_sukses = st.sidebar.slider("Estimasi Promo Berhasil (%)", min_value=10, max_value=100, value=50, step=10) / 100

# 5. Logika Finansial (Menghitung ROI)
# Kita hanya menargetkan promo kepada pelanggan yang ditebak akan CHURN (Predicted_Churn == 1)
target_pelanggan = hasil_df[hasil_df['Predicted_Churn'] == 1]
total_biaya_kampanye = len(target_pelanggan) * biaya_promo

# Menghitung pelanggan yang berhasil diselamatkan (True Positives)
pelanggan_diselamatkan = target_pelanggan[target_pelanggan['Actual_Churn'] == 1]
pendapatan_diselamatkan = pelanggan_diselamatkan['MonthlyCharge'].sum() * tingkat_sukses

# Keuntungan Bersih (Net Profit)
keuntungan_bersih = pendapatan_diselamatkan - total_biaya_kampanye

# 6. Menampilkan Hasil Visual di Layar Utama
st.markdown("### 📊 Ringkasan Dampak Finansial")
col1, col2, col3 = st.columns(3)

col1.metric("Biaya Kampanye (Cost)", f"${total_biaya_kampanye:,.2f}")
col2.metric("Pendapatan Diselamatkan", f"${pendapatan_diselamatkan:,.2f}")

# Jika untung warnanya hijau, jika rugi warnanya merah
col3.metric("Keuntungan Bersih (ROI AI)", f"${keuntungan_bersih:,.2f}", delta=f"${keuntungan_bersih:,.2f}")

st.markdown("---")
st.write("Formula Keuntungan:")
st.latex(r"\text{Keuntungan Bersih} = (\text{Total Tagihan Pelanggan Terselamatkan} \times \text{Tingkat Sukses}) - \text{Total Biaya Promo}")

st.write("### 📋 Detail Pelanggan Prioritas (Target Promo)")
st.write("Tabel di bawah berisi daftar pelanggan yang wajib segera dihubungi oleh tim *Customer Service*.")
st.dataframe(target_pelanggan.sort_values(by='MonthlyCharge', ascending=False).head(10))