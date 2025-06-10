import streamlit as st

# Judul aplikasi dan deskripsi
st.title("Logika Investasi Sederhana")
st.write("Penalaran logika ini dibuat untuk menghitung resiko kamu dalam berinvestasi.")

with st.form("LOGIC"):

    # Gaji
    gaji_rendah = range(0, 1000000)
    gaji_sedang = range(1000001, 5000000)
    gaji_besar  = range(5000001, 10000000)
    
    # Input Pendapatan
    pertanyaan_1 = st.subheader("Berapa Penghasilan Perbulan?")
    masukan_angka = st.number_input("Masukan Angka Lalu 'Enter'")
    st.write("NOTES: Min Rp 0 dan Max Rp 10.000.000. Masukan angka tanpa koma atau titik, contoh: '900000'.")
    # Jenis Kelamin
    pertanyaan_2 = st.subheader("Pilih Gender")
    opsi_lp = ["Laki-laki", "Perempuan"]
    masukan_lp = st.selectbox("Pilih Salah Satu", opsi_lp)

    # Input Umur
    pertanyaan_3 = st.subheader("Berapa Usia-mu Saat Ini")
    opsi_u = ["≤ 17 tahun", "18 - 25 tahun", "25 - 30 tahun", "30 tahun ≥"]
    umur = st.select_slider("Masukan Umur", opsi_u)

    konfirmasi = st.form_submit_button("Konfirmasi")
    # Gaji rendah - besar dan ≤ 17 tahun
    if konfirmasi:
        if masukan_angka in gaji_rendah :
            if masukan_lp == "Laki-laki":
                if umur == "≤ 17 tahun" :
                    st.success("""Modal yang dimiliki belum cukup. 
                               Cari pekerjaan dan penghasilan tetap terlebih dahulu, 
                               dan utamakan tabungan sebagai dana darurat 3-6 bulan pendapatan.""")
    if konfirmasi:
        if masukan_angka in gaji_rendah :
            if masukan_lp == "Perempuan":
                if umur == "≤ 17 tahun" :
                    st.success("""Modal yang dimiliki belum cukup. 
                               Cari pekerjaan dan penghasilan tetap terlebih dahulu, 
                               dan utamakan tabungan sebagai dana darurat 3-6 bulan pendapatan.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang :
            if masukan_lp == "Laki-laki":
                if umur == "≤ 17 tahun" :
                    st.success("""Utamakan perbesar income dan buat budgeting bulanan terukur. 
                               Silahkan investasi dengan alokasi uang dingin 10% dari pendapatan.
                               Atau opsi paling aman, tabung saja jika masih belum punya dana darurat 3-6 bulan pendapatan""")
    if konfirmasi:
        if masukan_angka in gaji_sedang :
            if masukan_lp == "Perempuan":
                if umur == "≤ 17 tahun" :
                    st.success("""Utamakan perbesar income dan buat budgeting bulanan terukur. 
                               Silahkan investasi dengan alokasi uang dingin 5% dari pendapatan.
                               Atau opsi paling aman, tabung saja jika masih belum punya dana darurat 3-6 bulan pendapatan""")
    if konfirmasi:
        if masukan_angka in gaji_besar  :
            if masukan_lp == "Laki-laki":
                if umur == "≤ 17 tahun" :
                    st.success("""Pastikan kamu sudah memiliki dana darurat 3-6 bulan pendapatan.
                               Silahkan investasi dengan alokasi uang dingin 10% - 15% dari pendapatan.""")
    if konfirmasi:
        if masukan_angka in gaji_besar  :
            if masukan_lp == "Perempuan":
                if umur == "≤ 17 tahun" :
                    st.success("""Pastikan kamu sudah memiliki dana darurat 3-6 bulan pendapatan.
                               Silahkan investasi dengan alokasi uang dingin 10% dari pendapatan.""")
    # Gaji rendah - besar dan 18 - 25 tahun
    if konfirmasi:
        if masukan_angka in gaji_rendah     :
            if masukan_lp == "Laki-laki"    :
                if umur == "18 - 25 tahun"  :
                    st.success("""Fokus utama adalah perbesar penghasilan dan belajar skill baru untuk meningkatkan value diri.
                               Jika sudah ada dana darurat, bisa mulai investasi dengan tingkat agresivitas 30-40%.
                               Prioritaskan membangun tabungan dana darurat 3-6 bulan pendapatan terlebih dahulu.""")
    if konfirmasi:
        if masukan_angka in gaji_rendah     :
            if masukan_lp == "Perempuan"    :
                if umur == "18 - 25 tahun"  :
                    st.success("""Fokus utama adalah perbesar penghasilan dan kembangkan karir untuk stabilitas finansial.
                               Jika sudah ada dana darurat, bisa mulai investasi dengan tingkat agresivitas 15-25%.
                               Prioritaskan membangun dana darurat 3-6 bulan pendapatan sebelum investasi.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang     :
            if masukan_lp == "Laki-laki"    :
                if umur == "18 - 25 tahun"  :
                    st.success("""Ini saat yang tepat untuk balance antara perbesar income dan investasi.
                               Pastikan sudah ada dana darurat 3-6 bulan pendapatan, lalu investasi dengan tingkat agresivitas 30-40%.
                               Alokasikan 15-20% dari pendapatan untuk investasi jangka panjang.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang     :
            if masukan_lp == "Perempuan"    :
                if umur == "18 - 25 tahun"  :
                    st.success("""Saat yang tepat untuk mulai serius berinvestasi setelah memiliki dana darurat.
                               Pastikan sudah ada dana darurat 3-6 bulan pendapatan, lalu investasi dengan tingkat agresivitas 15-25%.
                               Alokasikan 10-15% dari pendapatan untuk investasi dengan strategi konservatif.""")
    if konfirmasi:
        if masukan_angka in gaji_besar      :
            if masukan_lp == "Laki-laki"    :
                if umur == "18 - 25 tahun"  :
                    st.success("""Mantap! Dengan income yang baik di usia muda, manfaatkan untuk investasi agresif.
                               Pastikan dana darurat 3-6 bulan sudah ada, lalu investasi 15-20% dari pendapatan.
                               Tingkat agresivitas investasi bisa 30-40% untuk memaksimalkan compound interest.""")
    if konfirmasi:
        if masukan_angka in gaji_besar      :
            if masukan_lp == "Perempuan"    :
                if umur == "18 - 25 tahun"  :
                    st.success("""Excellent! Dengan penghasilan yang baik, saatnya membangun wealth jangka panjang.
                               Pastikan dana darurat 3-6 bulan sudah tersedia, lalu investasi 10-15% dari pendapatan.
                               Tingkat agresivitas investasi 15-25% dengan fokus pada instrumen yang stabil.""")
    # Gaji rendah - besar dan 25 - 30 tahun
    if konfirmasi:
        if masukan_angka in gaji_rendah     :
            if masukan_lp == "Laki-laki"    :
                if umur == "25 - 30 tahun"  :
                    st.success("""Di usia ini, fokus pada peningkatan skill dan karir untuk naik income level.
                               Jika ada dana darurat, investasi dengan tingkat agresivitas 20-30% masih memungkinkan.
                               Prioritas utama tetap pada stabilitas keuangan dan peningkatan penghasilan.""")
    if konfirmasi:
        if masukan_angka in gaji_rendah     :
            if masukan_lp == "Perempuan"    :
                if umur == "25 - 30 tahun"  :
                    st.success("""Saatnya serius merencanakan keuangan jangka panjang. Fokus perbesar income terlebih dahulu.
                               Jika sudah memiliki dana darurat, mulai investasi konservatif dengan agresivitas 10-20%.
                               Pertimbangkan juga perencanaan untuk masa depan keluarga.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang     :
            if masukan_lp == "Laki-laki"    :
                if umur == "25 - 30 tahun"  :
                    st.success("""Usia golden untuk balance income growth dan investasi serius.
                               Pastikan dana darurat 3-6 bulan tersedia, lalu investasi dengan agresivitas 20-30%.
                               Alokasikan 15-18% dari pendapatan untuk investasi jangka menengah-panjang.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang     :
            if masukan_lp == "Perempuan"    :
                if umur == "25 - 30 tahun"  :
                    st.success("""Waktu yang tepat untuk membangun portfolio investasi yang solid.
                               Pastikan dana darurat 3-6 bulan sudah siap, lalu investasi dengan agresivitas 10-20%.
                               Alokasikan 12-15% dari pendapatan untuk investasi dengan strategi balanced.""")
    if konfirmasi:
        if masukan_angka in gaji_besar      :
            if masukan_lp == "Laki-laki"    :
                if umur == "25 - 30 tahun"  :
                    st.success("""Perfect timing untuk serious wealth building! Income yang baik harus dioptimalkan.
                               Dengan dana darurat terjamin, investasi 15-20% dari pendapatan dengan agresivitas 20-30%.
                               Mulai diversifikasi portfolio untuk tujuan finansial jangka panjang.""")
    if konfirmasi:
        if masukan_angka in gaji_besar      :
            if masukan_lp == "Perempuan"    :
                if umur == "25 - 30 tahun"  :
                    st.success("""Excellent position untuk membangun kekayaan jangka panjang!
                               Dengan dana darurat yang solid, investasi 15-18% dari pendapatan dengan agresivitas 10-20%.
                               Fokus pada strategi investasi yang balanced untuk mencapai financial independence.""")
    # Gaji rendah - besar dan 30 tahun ≥
    if konfirmasi:
        if masukan_angka in gaji_rendah :
            if masukan_lp == "Laki-laki":
                if umur == "30 tahun ≥" :
                    st.success("""Di usia ini, prioritas utama adalah stabilitas finansial dan perencanaan masa depan.
                               Fokus pada peningkatan skill untuk menaikkan income. Jika ada dana darurat, investasi konservatif dengan agresivitas 20-25%.
                               Pertimbangkan juga proteksi asuransi untuk keluarga.""")
    if konfirmasi:
        if masukan_angka in gaji_rendah :
            if masukan_lp == "Perempuan":
                if umur == "30 tahun ≥" :
                    st.success("""Saatnya fokus pada stabilitas dan perencanaan jangka panjang untuk keluarga.
                               Utamakan peningkatan penghasilan dan bangun dana darurat yang kuat.
                               Jika sudah ada dana darurat, investasi konservatif dengan agresivitas 10% saja.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang :
            if masukan_lp == "Laki-laki":
                if umur == "30 tahun ≥" :
                    st.success("""Usia yang tepat untuk serious financial planning dengan pendekatan yang lebih konservatif.
                               Pastikan dana darurat 3-6 bulan solid, lalu investasi 15-18% dengan agresivitas 20-25%.
                               Mulai pikirkan diversifikasi untuk tujuan retirement dan pendidikan anak.""")
    if konfirmasi:
        if masukan_angka in gaji_sedang :
            if masukan_lp == "Perempuan":
                if umur == "30 tahun ≥" :
                    st.success("""Waktu untuk fokus pada investasi yang lebih stabil dan terencana.
                               Dengan dana darurat yang kuat, investasi 12-15% dari pendapatan dengan agresivitas konservatif 10%.
                               Prioritaskan instrumen investasi yang aman untuk tujuan jangka panjang.""")
    if konfirmasi:
        if masukan_angka in gaji_besar  :
            if masukan_lp == "Laki-laki":
                if umur == "30 tahun ≥" :
                    st.success("""Excellent! Dengan income besar di usia mature, saatnya optimalisasi wealth management.
                               Dana darurat harus sudah solid, investasi 15-20% dengan agresivitas 20-25%.
                               Fokus pada diversifikasi portfolio dan perencanaan retirement yang matang.""")
    if konfirmasi:
        if masukan_angka in gaji_besar  :
            if masukan_lp == "Perempuan":
                if umur == "30 tahun ≥" :
                    st.success("""Perfect position untuk wealth preservation dan growth yang stabil!
                               Dengan dana darurat yang memadai, investasi 15-18% dengan strategi konservatif agresivitas 10%.
                               Fokus pada instrumen investasi yang memberikan return stabil untuk tujuan jangka panjang.""")
    elif konfirmasi:
        st.warning("NIRFUNGSI!")