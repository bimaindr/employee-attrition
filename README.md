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

```
## Business Dashboard

Business dashboard yang dibuat bertujuan untuk membantu manajemen dan departemen HR dalam memahami pola attrition karyawan secara visual dan mudah dipahami, tanpa harus membaca data mentah atau tabel yang kompleks.

Dashboard dikembangkan menggunakan Metabase dan terhubung langsung ke database PostgreSQL yang berisi data karyawan hasil pengolahan dan feature engineering. Visualisasi yang ditampilkan difokuskan pada faktor-faktor utama yang memengaruhi tingginya attrition rate, sehingga dapat digunakan sebagai dasar pengambilan keputusan strategis.

1. Attrition berdasarkan Over Time
Visualisasi ini menunjukkan bahwa karyawan yang sering lembur (Over Time = Yes) memiliki tingkat attrition yang lebih tinggi dibandingkan karyawan yang tidak lembur. Hal ini mengindikasikan bahwa beban kerja berlebih berpotensi meningkatkan risiko karyawan untuk keluar.

2. Attrition berdasarkan Rata-rata Pendapatan (Average Income)
Grafik distribusi menunjukkan bahwa attrition lebih banyak terjadi pada kelompok karyawan dengan pendapatan yang relatif lebih rendah. Semakin tinggi pendapatan rata-rata, kecenderungan attrition cenderung menurun.

3. Attrition berdasarkan Job Role
Visualisasi ini memperlihatkan job role dengan jumlah attrition tertinggi, seperti Sales Executive dan Research Scientist. Informasi ini penting bagi HR untuk memfokuskan kebijakan retensi pada posisi yang paling rentan.

4. Attrition berdasarkan Department
Departemen Research & Development dan Sales menunjukkan tingkat attrition yang lebih tinggi dibandingkan departemen lainnya, sehingga perlu mendapat perhatian khusus dari manajemen.

5. Perbandingan Total Employee, Total Attrition, dan Attrition Rate per Job Role
Visualisasi kombinasi ini membantu melihat hubungan antara jumlah karyawan, jumlah attrition, dan tingkat attrition secara bersamaan untuk setiap job role.

## Conclusion

Berdasarkan seluruh tahapan yang telah dilakukan dalam proyek ini, dapat disimpulkan bahwa pendekatan data science mampu memberikan solusi yang efektif untuk membantu perusahaan Edutech dalam menangani permasalahan attrition karyawan.

Melalui proses eksplorasi data dan visualisasi, proyek ini berhasil mengidentifikasi beberapa faktor utama yang berkontribusi terhadap tingginya attrition, seperti overtime, tingkat pendapatan, job role, departemen, kepuasan kerja, dan work-life balance. Temuan ini diperkuat dengan hasil dashboard yang memberikan gambaran kondisi attrition secara komprehensif dan mudah dipahami oleh stakeholder non-teknis.

Selain itu, model machine learning berbasis Logistic Regression yang dikembangkan mampu memprediksi probabilitas attrition karyawan secara individual. Model ini dapat dimanfaatkan oleh departemen HR sebagai early warning system untuk mengidentifikasi karyawan yang berisiko tinggi keluar, sehingga perusahaan dapat mengambil tindakan preventif lebih awal.

### Rekomendasi Action Items (Optional)

- Mengurangi beban lembur (Over Time) dengan melakukan evaluasi distribusi kerja, khususnya pada job role dan departemen dengan tingkat attrition tinggi.

- Melakukan evaluasi dan penyesuaian kompensasi bagi karyawan dengan pendapatan rendah yang berada pada posisi berisiko tinggi attrition.

- Menyusun program retensi khusus untuk job role dan departemen dengan tingkat attrition tertinggi, seperti Sales dan Research & Development.

- Meningkatkan job satisfaction dan work-life balance, misalnya melalui fleksibilitas kerja, pelatihan, atau program kesejahteraan karyawan.

- Memanfaatkan model prediksi attrition secara berkala untuk memantau karyawan berisiko dan mendukung pengambilan keputusan HR secara preventif.
