# 💰 Logika Investasi Sederhana

Aplikasi web berbasis Streamlit yang membantu pengguna mendapatkan rekomendasi investasi personal berdasarkan profil keuangan dan demografis mereka.

## 🚀 Fitur Utama

- **Analisis Profil Keuangan**: Evaluasi berdasarkan penghasilan bulanan (Rp 0 - Rp 10.000.000)
- **Personalisasi Gender**: Rekomendasi yang disesuaikan untuk laki-laki dan perempuan
- **Segmentasi Usia**: Strategi berbeda untuk setiap rentang usia
- **Literasi Keuangan**: Edukasi singkat tentang investasi dan perencanaan keuangan
- **Validasi Input**: Sistem peringatan untuk input yang tidak valid

## 📊 Kategori Penghasilan

| Kategori | Rentang Penghasilan | Fokus Utama |
|----------|-------------------|-------------|
| **Gaji Rendah** | Rp 0 - Rp 999.999 | Perbesar income, bangun dana darurat |
| **Gaji Sedang** | Rp 1.000.000 - Rp 4.999.999 | Balance income growth & investasi |
| **Gaji Besar** | Rp 5.000.000 - Rp 10.000.000 | Fokus investasi & wealth building |

## 🎯 Tingkat Agresivitas Investasi

### Berdasarkan Usia dan Gender

| Rentang Usia | Laki-laki | Perempuan |
|--------------|-----------|-----------|
| **18-25 tahun** | 30-40% | 15-25% |
| **25-30 tahun** | 20-30% | 10-20% |
| **30+ tahun** | 20-25% | 10% |

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Streamlit** - Framework web app
- **HTML/CSS** - Styling (built-in Streamlit)

## 📋 Prasyarat

Pastikan Anda telah menginstall:
- Python 3.7 atau lebih baru
- pip (Python package installer)

## ⚡ Instalasi & Menjalankan Aplikasi

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/username/logika-investasi-sederhana.git
   cd logika-investasi-sederhana
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit
   ```

3. **Jalankan aplikasi:**
   ```bash
   streamlit run app.py
   ```

4. **Buka browser dan akses:**
   ```
   http://localhost:8501
   ```

## 🎮 Cara Penggunaan

1. **Input Penghasilan**: Masukkan penghasilan bulanan Anda (tanpa titik atau koma)
   - Contoh: `2500000` untuk Rp 2.500.000

2. **Pilih Gender**: Pilih jenis kelamin Anda dari dropdown menu

3. **Tentukan Usia**: Pilih rentang usia Anda menggunakan slider:
   - ≤ 17 tahun
   - 18 - 25 tahun  
   - 25 - 30 tahun
   - 30 tahun ≥

4. **Klik Konfirmasi**: Sistem akan memberikan rekomendasi personal

## 📖 Contoh Output

### Untuk Penghasilan Sedang, Laki-laki, Usia 25-30 tahun:
```
Usia golden untuk balance income growth dan investasi serius.
Pastikan dana darurat 3-6 bulan tersedia, lalu investasi dengan agresivitas 20-30%.
Alokasikan 15-18% dari pendapatan untuk investasi jangka menengah-panjang.
```

## 🔧 Struktur Kode

```
logika-investasi-sederhana/
│
├── app.py              # File utama aplikasi Streamlit
├── README.md           # Dokumentasi proyek
└── requirements.txt    # Dependencies (opsional)
```

## 🏗️ Logika Aplikasi

Aplikasi menggunakan sistem kondisional bersarang yang mempertimbangkan:

1. **Validasi Input**: Memastikan penghasilan dalam rentang yang valid
2. **Kategorisasi**: Mengklasifikasikan pengguna berdasarkan 3 parameter
3. **Algoritma Rekomendasi**: Memberikan saran berdasarkan kombinasi parameter
4. **Error Handling**: Menampilkan peringatan untuk input tidak valid

## 🎯 Prinsip Rekomendasi

### Dana Darurat Pertama
- Semua rekomendasi mengutamakan dana darurat 3-6 bulan pendapatan
- Investasi baru dilakukan setelah dana darurat terpenuhi

### Alokasi Investasi
- **Gaji Rendah**: Fokus stabilitas, investasi minimal
- **Gaji Sedang**: 10-18% dari pendapatan
- **Gaji Besar**: 15-20% dari pendapatan

### Faktor Usia
- **Usia Muda**: Lebih agresif, fokus growth
- **Usia Menengah**: Balanced approach
- **Usia Tua**: Konservatif, fokus preservation

## 📈 Pengembangan Selanjutnya

- [ ] Integrasi dengan API keuangan real-time
- [ ] Kalkulator dana darurat otomatis
- [ ] Rekomendasi instrumen investasi spesifik
- [ ] Grafik visualisasi portfolio
- [ ] Export hasil ke PDF
- [ ] Multi-language support

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Kontak

**Developer**: [Rico Cahyo Saputro]
- Email: ric*****@gmail.com
- LinkedIn: n/A
- GitHub: [@KulinAja](https://github.com/username)

## ⭐ Dukung Proyek Ini

Jika aplikasi ini membantu Anda, jangan lupa berikan ⭐ pada repository ini!

---

**Disclaimer**: Aplikasi ini hanya memberikan rekomendasi umum untuk edukasi. Konsultasikan dengan advisor keuangan profesional untuk keputusan investasi yang lebih kompleks.

## 📸 Screenshot

![App Screenshot](screenshot.png)
*Screenshot aplikasi Logika Investasi Sederhana*
