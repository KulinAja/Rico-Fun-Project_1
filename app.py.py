import streamlit as st

st.title("Logika Investasi Sederhana")
st.write("Penalaran logika ini dibuat untuk menghitung resiko kamu dalam berinvestasi.")

def get_gaji_level(gaji):
    if 0 <= gaji <= 1_000_000:
        return "rendah"
    elif 1_000_001 <= gaji <= 5_000_000:
        return "sedang"
    elif 5_000_001 <= gaji <= 10_000_000:
        return "besar"
    else:
        return None

ADVICE = {
    # (gaji_level, gender, umur): "advice string"\
    # kelompok "rendah"
    ("rendah", "Laki-laki", "≤ 17 tahun"): "Modal yang dimiliki belum cukup. Cari pekerjaan dan penghasilan tetap terlebih dahulu, dan utamakan tabungan sebagai dana darurat 3-6 bulan pendapatan.",
    ("rendah", "Perempuan", "≤ 17 tahun"): "Modal yang dimiliki belum cukup. Cari pekerjaan dan penghasilan tetap terlebih dahulu, dan utamakan tabungan sebagai dana darurat 3-6 bulan pendapatan.",
    ("rendah", "Laki-laki", "18 - 25 tahun"): "Fokus utama adalah perbesar penghasilan dan belajar skill baru untuk meningkatkan value diri. Jika sudah ada dana darurat, bisa mulai investasi dengan tingkat agresivitas 30-40%. Prioritaskan membangun tabungan dana darurat 3-6 bulan pendapatan terlebih dahulu.",
    ("rendah", "Perempuan", "18 - 25 tahun"): "Fokus utama adalah perbesar penghasilan dan kembangkan karir untuk stabilitas finansial. Jika sudah ada dana darurat, bisa mulai investasi dengan tingkat agresivitas 15-25%. Prioritaskan membangun dana darurat 3-6 bulan pendapatan sebelum investasi.",
    ("rendah", "Laki-laki", "25 - 30 tahun"): "Di usia ini, fokus pada peningkatan skill dan karir untuk naik income level. Jika ada dana darurat, investasi dengan tingkat agresivitas 20-30% masih memungkinkan. Prioritas utama tetap pada stabilitas keuangan dan peningkatan penghasilan.",
    ("rendah", "Perempuan", "25 - 30 tahun"): "Saatnya serius merencanakan keuangan jangka panjang. Fokus perbesar income terlebih dahulu. Jika sudah memiliki dana darurat, mulai investasi konservatif dengan agresivitas 10-20%. Pertimbangkan juga perencanaan untuk masa depan keluarga.",
    ("rendah", "Laki-laki", "30 tahun ≥"): "Di usia ini, prioritas utama adalah stabilitas finansial dan perencanaan masa depan. Fokus pada peningkatan skill untuk menaikkan income. Jika ada dana darurat, investasi konservatif dengan agresivitas 20-25%. Pertimbangkan juga proteksi asuransi untuk keluarga.",
    ("rendah", "Perempuan", "30 tahun ≥"): "Saatnya fokus pada stabilitas dan perencanaan jangka panjang untuk keluarga. Utamakan peningkatan penghasilan dan bangun dana darurat yang kuat. Jika sudah ada dana darurat, investasi konservatif dengan agresivitas 10% saja.",
    # kelompok "sedang"
    ("sedang", "Laki-laki", "≤ 17 tahun"): "Utamakan perbesar income dan buat budgeting bulanan terukur. Silahkan investasi dengan alokasi uang dingin 10% dari pendapatan. Atau opsi paling aman, tabung saja jika masih belum punya dana darurat 3-6 bulan pendapatan.",
    ("sedang", "Perempuan", "≤ 17 tahun"): "Utamakan perbesar income dan buat budgeting bulanan terukur. Silahkan investasi dengan alokasi uang dingin 5% dari pendapatan. Atau opsi paling aman, tabung saja jika masih belum punya dana darurat 3-6 bulan pendapatan.",
    ("sedang", "Laki-laki", "18 - 25 tahun"): "Ini saat yang tepat untuk balance antara perbesar income dan investasi. Pastikan sudah ada dana darurat 3-6 bulan pendapatan, lalu investasi dengan tingkat agresivitas 30-40%. Alokasikan 15-20% dari pendapatan untuk investasi jangka panjang.",
    ("sedang", "Perempuan", "18 - 25 tahun"): "Saat yang tepat untuk mulai serius berinvestasi setelah memiliki dana darurat. Pastikan sudah ada dana darurat 3-6 bulan pendapatan, lalu investasi dengan tingkat agresivitas 15-25%. Alokasikan 10-15% dari pendapatan untuk investasi dengan strategi konservatif.",
    ("sedang", "Laki-laki", "25 - 30 tahun"): "Usia golden untuk balance income growth dan investasi serius. Pastikan dana darurat 3-6 bulan tersedia, lalu investasi dengan agresivitas 20-30%. Alokasikan 15-18% dari pendapatan untuk investasi jangka menengah-panjang.",
    ("sedang", "Perempuan", "25 - 30 tahun"): "Waktu yang tepat untuk membangun portfolio investasi yang solid. Pastikan dana darurat 3-6 bulan sudah siap, lalu investasi dengan agresivitas 10-20%. Alokasikan 12-15% dari pendapatan untuk investasi dengan strategi balanced.",
    ("sedang", "Laki-laki", "30 tahun ≥"): "Usia yang tepat untuk serious financial planning dengan pendekatan yang lebih konservatif. Pastikan dana darurat 3-6 bulan solid, lalu investasi 15-18% dengan agresivitas 20-25%. Mulai pikirkan diversifikasi untuk tujuan retirement dan pendidikan anak.",
    ("sedang", "Perempuan", "30 tahun ≥"): "Waktu untuk fokus pada investasi yang lebih stabil dan terencana. Dengan dana darurat yang kuat, investasi 12-15% dari pendapatan dengan agresivitas konservatif 10%. Prioritaskan instrumen investasi yang aman untuk tujuan jangka panjang.",
    # kelompok "besar"
    ("besar", "Laki-laki", "≤ 17 tahun"): "Pastikan kamu sudah memiliki dana darurat 3-6 bulan pendapatan. Silahkan investasi dengan alokasi uang dingin 10% - 15% dari pendapatan.",
    ("besar", "Perempuan", "≤ 17 tahun"): "Pastikan kamu sudah memiliki dana darurat 3-6 bulan pendapatan. Silahkan investasi dengan alokasi uang dingin 10% dari pendapatan.",
    ("besar", "Laki-laki", "18 - 25 tahun"): "Mantap! Dengan income yang baik di usia muda, manfaatkan untuk investasi agresif. Pastikan dana darurat 3-6 bulan sudah ada, lalu investasi 15-20% dari pendapatan. Tingkat agresivitas investasi bisa 30-40% untuk memaksimalkan compound interest.",
    ("besar", "Perempuan", "18 - 25 tahun"): "Excellent! Dengan penghasilan yang baik, saatnya membangun wealth jangka panjang. Pastikan dana darurat 3-6 bulan sudah tersedia, lalu investasi 10-15% dari pendapatan. Tingkat agresivitas investasi 15-25% dengan fokus pada instrumen yang stabil.",
    ("besar", "Laki-laki", "25 - 30 tahun"): "Perfect timing untuk serious wealth building! Income yang baik harus dioptimalkan. Dengan dana darurat terjamin, investasi 15-20% dari pendapatan dengan agresivitas 20-30%. Mulai diversifikasi portfolio untuk tujuan finansial jangka panjang.",
    ("besar", "Perempuan", "25 - 30 tahun"): "Excellent position untuk membangun kekayaan jangka panjang! Dengan dana darurat yang solid, investasi 15-18% dari pendapatan dengan agresivitas 10-20%. Fokus pada strategi investasi yang balanced untuk mencapai financial independence.",
    ("besar", "Laki-laki", "30 tahun ≥"): "Excellent! Dengan income besar di usia mature, saatnya optimalisasi wealth management. Dana darurat harus sudah solid, investasi 15-20% dengan agresivitas 20-25%. Fokus pada diversifikasi portfolio dan perencanaan retirement yang matang.",
    ("besar", "Perempuan", "30 tahun ≥"): "Perfect position untuk wealth preservation dan growth yang stabil! Dengan dana darurat yang memadai, investasi 15-18% dengan strategi konservatif agresivitas 10%. Fokus pada instrumen investasi yang memberikan return stabil untuk tujuan jangka panjang."
    # ... Tambahkan kombinasi lain sesuai kebutuhan ...
}

with st.form("LOGIC"):
    masukan_angka = st.number_input("Masukan Penghasilan Perbulan (Rp)", min_value=0, max_value=10_000_000, step=1)
    st.write("NOTES: Min Rp 0 dan Max Rp 10.000.000. Masukan angka tanpa koma atau titik, contoh: '900000'.")
    opsi_lp = ["Laki-laki", "Perempuan"]
    masukan_lp = st.selectbox("Pilih Gender", opsi_lp)
    opsi_u = ["≤ 17 tahun", "18 - 25 tahun", "25 - 30 tahun", "30 tahun ≥"]
    umur = st.select_slider("Masukan Umur", opsi_u)
    konfirmasi = st.form_submit_button("Konfirmasi")

    if konfirmasi:
        gaji_level = get_gaji_level(masukan_angka)
        key = (gaji_level, masukan_lp, umur)
        if gaji_level is None:
            st.warning("Masukan penghasilan harus antara 0 dan 10.000.000")
        elif key in ADVICE:
            st.success(ADVICE[key])
        else:
            st.warning("Belum ada saran untuk kombinasi input ini. Silakan konsultasi lebih lanjut.")

# Honorable mention kepada pak Yudy yang telah banyak memodifikasi logic isi pada mini projek ini, karena saya sadar mini projek awal yang saya buat sangatlah berantakan dan terlalu banyak terjadi pengulangan.