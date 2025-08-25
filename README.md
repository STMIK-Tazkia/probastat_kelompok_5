Analisis Tingkat Pengangguran di Indonesia
Proyek ini bertujuan untuk menganalisis dan memodelkan tingkat pengangguran di Indonesia dari data historis. Analisis ini menggunakan pendekatan visualisasi data
untuk memahami tren dan pemodelan regresi linear dengan optimasi Stochastic Gradient Descent (SGD) untuk memprediksi tingkat pengangguran.

Latar Belakang
Pengangguran adalah indikator ekonomi penting yang dapat memengaruhi 
kondisi sosial dan stabilitas suatu negara.Proyek ini memanfaatkan algoritma machine learning, khususnya Linear Regression yang 
dioptimalkan dengan Stochastic Gradient Descent (SGD), untuk memahami hubungan antara jumlah penduduk bekerja dan jumlah 
pengangguran dengan tingkat pengangguran secara keseluruhan.

Metodologi
Metodologi penelitian ini menggunakan pendekatan kuantitatif 
dengan eksperimen komputasional. Langkah-langkah yang dilakukan adalah sebagai berikut:

Pengumpulan Data: 
Menggunakan dataset data pengangguran.xlsx yang berisi data jumlah pengangguran dan jumlah penduduk bekerja.

Pra-pemrosesan Data: Menghitung tingkat pengangguran dalam persentase dan mengubah format tanggal menjadi tahun.

Visualisasi Data: 
Membuat grafik untuk memvisualisasikan tren tingkat pengangguran dari tahun ke tahun.

Pemodelan:
Membangun model regresi linear menggunakan SGDRegressor dari scikit-learn. Data dibagi menjadi data latih dan data uji dengan perbandingan 80:20.

Evaluasi Model:
Mengevaluasi performa model menggunakan metrik Mean Squared Error (MSE) dan R² Score.

Persyaratan Sistem
Pastikan Anda telah menginstal Python 3. Proyek ini membutuhkan beberapa pustaka (library) Python, yang dapat diinstal menggunakan pip:

Bash

pip install pandas matplotlib scikit-learn
Struktur File

data pengangguran.xlsx: Dataset yang digunakan untuk analisis.

pengangguran.py: Skrip Python untuk pra-pemrosesan dan visualisasi data.

SGD.py: Skrip Python untuk pemodelan regresi linear dengan SGD.

Cara Menjalankan Program
Untuk menjalankan analisis, Anda dapat mengeksekusi skrip Python secara berurutan.

1. Visualisasi Data
Jalankan skrip pengangguran.py untuk melihat tren tingkat pengangguran:

Bash

python pengangguran.py
Skrip ini akan menampilkan grafik tingkat pengangguran per tahun.

2. Pemodelan dan Prediksi
Jalankan skrip SGD.py untuk melatih model dan melihat hasilnya:

Bash

python SGD.py
Skrip ini akan mencetak nilai MSE dan R² dari model yang telah dilatih.

Hasil dan Analisis

Visualisasi: Grafik menunjukkan tren pengangguran yang berfluktuasi dari tahun ke tahun.

Performa Model: Model Linear Regression dengan optimasi SGD menunjukkan 
performa yang cepat dan efisien. Nilai R² yang dihasilkan mendekati 0.9, yang menandakan model cukup baik 
dalam menjelaskan variasi data. Rata-rata kesalahan (MSE) yang rendah juga menunjukkan prediksi yang akurat.

Kesimpulan
Penelitian ini menyimpulkan bahwa algoritma Linear Regression dengan optimasi Stochastic Gradient Descent (SGD) dapat digunakan secara efektif untuk memprediksi tingkat pengangguran di Indonesia. Untuk penelitian di masa depan, disarankan untuk menggunakan dataset yang lebih besar dan membandingkan performa dengan model lain seperti Random Forest atau Neural Network.
