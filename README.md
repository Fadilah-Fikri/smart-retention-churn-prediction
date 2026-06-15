💸 Smart Retention: End-to-End Customer Churn Prediction dengan Cost-Benefit Analysis

📌 Ringkasan Proyek
Proyek ini membangun sebuah sistem prediksi customer churn (pelanggan berhenti berlangganan) berbasis Machine Learning yang terintegrasi langsung dengan Kalkulator Dampak Finansial (ROI). Solusi ini dikembangkan menggunakan dataset kustom IBM Telco Churn untuk membantu tim manajemen dan pemasaran (marketing) mengoptimalkan anggaran retensi secara efisien, dengan target menyelamatkan pendapatan yang berpotensi hilang akibat pelanggan yang pergi.

📉 Latar Belakang & Masalah Bisnis
Kehilangan pelanggan (churn) merupakan salah satu tantangan finansial terbesar di industri telekomunikasi. Analisis awal terhadap data historis menunjukkan potensi kerugian kotor yang sangat masif akibat pelanggan yang pindah ke kompetitor.

Tantangan utamanya adalah inefisiensi strategi retensi:

  1.  Jika perusahaan memberikan promo penahanan ke semua pelanggan, anggaran pemasaran akan membengkak secara sia-sia untuk orang yang sebenarnya tetap setia.

  2.  Jika perusahaan tidak melakukan tindakan apa pun, pendapatan dari pelanggan bernilai tinggi (high-value customers) akan hilang sepenuhnya.

🛠️ Alur Solusi & Teknologi (Tech Stack)
Proyek ini diselesaikan secara end-to-end menggunakan lingkungan lokal dengan Visual Studio Code (VS Code):

  ✅  Analisis & Manipulasi Data: Python, Pandas, NumPy.
  
  ✅  Visualisasi Data: Matplotlib, Seaborn (Menemukan bahwa pelanggan dengan kontrak bulanan/Month-to-month memiliki risiko churn paling tinggi).
  
  ✅  Machine Learning (AI): Scikit-Learn dengan algoritma Random Forest Classifier.
  
  ✅  Antarmuka Aplikasi Web (Deployment): Streamlit untuk membungkus model menjadi dasbor interaktif yang bisa digunakan langsung oleh tim bisnis.

📊 Hasil Evaluasi Model Machine Learning
Model AI dilatih menggunakan proporsi pembagian data 80% (Training) dan 20% (Testing). Karena ketidakseimbangan kelas (imbalanced data), model dioptimalkan menggunakan bobot kelas seimbang (balanced class weights).

  ✅  Metrik Utama (Recall & F1-Score): Fokus utama model adalah meminimalkan False Negatives (gagal mendeteksi pelanggan yang sebenarnya mau kabur), sehingga metrik Recall dioptimalkan untuk memastikan sebagian besar pelanggan berisiko tinggi dapat terjaring oleh sistem.
  
  ✅  Aplikasi Praktis: Model berhasil mengekstrak daftar pelanggan prioritas yang memiliki probabilitas churn tertinggi lengkap dengan nilai tagihan bulanan (MonthlyCharge) mereka untuk segera ditindaklanjuti oleh tim Customer Service.

💰 Dampak Finansial & Simulasi Bisnis (Cost-Benefit Analysis)
Keunikan utama dari proyek ini adalah visualisasi performa teknis model ke dalam nilai mata uang nyata yang interaktif pada dasbor Streamlit:

  1.  Skenario Tanpa AI: Perusahaan menanggung kerugian penuh dari total tagihan bulanan pelanggan yang pergi tanpa adanya upaya pencegahan terarah.
  2.  Skenario Dengan AI (Smart Retention): Anggaran pemasaran dialokasikan secara presisi. Biaya promo (misalnya $20/pelanggan) hanya diberikan kepada pelanggan yang terdeteksi oleh AI akan churn.
  3.  Return on Investment (ROI): Dengan mengasumsikan tingkat keberhasilan promo sebesar 50%, dasbor berhasil membuktikan secara matematis bahwa implementasi model AI ini mampu menghasilkan Keuntungan Bersih (Net Profit/Revenue Saved) yang signifikan dibandingkan melakukan kampanye promosi secara acak atau tidak melakukan pencegahan sama sekali.

💡 Kesimpulan Portofolio
Proyek ini membuktikan kompetensi seorang Data Scientist tidak hanya dalam aspek teknis penulisan kode atau evaluasi metrik akurasi, melainkan juga dalam kemampuan Business Storytelling—yaitu menerjemahkan prediksi probabilitas machine learning menjadi keputusan taktis yang menyelamatkan finansial perusahaan.
