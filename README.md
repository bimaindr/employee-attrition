# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan menghadapi tantangan dalam mengelola sumber daya manusia, khususnya terkait tingginya tingkat attrition (keluar masuk karyawan). Tingginya attrition dapat menyebabkan berbagai dampak negatif, seperti meningkatnya biaya rekrutmen dan pelatihan, menurunnya produktivitas tim, serta terganggunya stabilitas operasional dan budaya kerja perusahaan.

Oleh karena itu, perusahaan membutuhkan pendekatan berbasis data untuk memahami pola attrition, mengidentifikasi faktor-faktor yang memengaruhi keputusan karyawan untuk keluar, serta memprediksi potensi attrition di masa depan. Dengan pemanfaatan data historis karyawan dan teknik data science, perusahaan diharapkan dapat mengambil keputusan strategis yang lebih tepat dalam meningkatkan retensi karyawan.

### Permasalahan Bisnis
Berdasarkan kondisi tersebut, permasalahan bisnis yang ingin diselesaikan dalam proyek ini antara lain:

1. Perusahaan belum mengetahui faktor utama yang memengaruhi tingginya attrition rate.

2. Tidak adanya visualisasi data yang informatif untuk membantu manajemen memahami kondisi attrition berdasarkan departemen, jabatan, kepuasan kerja, dan faktor lainnya.

3. Kesulitan dalam mengidentifikasi karyawan yang berpotensi keluar lebih awal.

4. Belum tersedia model prediksi yang dapat digunakan oleh departemen HR sebagai alat bantu pengambilan keputusan.

5. Pengambilan kebijakan HR masih bersifat reaktif, bukan preventif berbasis data.

### Cakupan Proyek
Cakupan proyek yang dikerjakan dalam analisis ini meliputi:

1. Pengolahan dan eksplorasi data karyawan, termasuk pembersihan data dan feature engineering.

2. Analisis faktor-faktor yang memengaruhi attrition, seperti:
    - Department dan Job Role
    - Job Level
    - Monthly Income
    - Job Satisfaction
    - Work Life Balance
    - Over Time
    - Lama bekerja dan promosi

3. Pembuatan query SQL untuk mendukung analisis data dan kebutuhan visualisasi.

4. Pembuatan dashboard interaktif menggunakan Metabase yang menampilkan:
    - Attrition rate
    - Distribusi attrition berdasarkan faktor-faktor utama
    - Visualisasi grafik

3. Pengembangan model machine learning (Logistic Regression) untuk memprediksi kemungkinan attrition karyawan.

4. Pembuatan script Python sederhana (.py) untuk menjalankan proses prediksi dan menghasilkan output probabilitas attrition.

5. Penyimpanan dan pemanfaatan model untuk mendukung analisis dan pengambilan keputusan oleh departemen HR.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:

```
conda create --name penerapan-data-science python=3.9
conda activate penerapan-data-science
pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn==1.2.2 joblib==1.3.1
pip install psycopg2
docker pull metabase/metabase:v0.46.4
docker run -p 3000:3000 --name metabase metabase/metabase

```

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
