
if __name__ == "__main__":
    import main

def inputBiodata():
    print("=== Masukkan Biodata Anda ===")
    nama = input("Nama: ")
    
    # Validasi umur agar pasti berupa angka (integer)
    while True:
        try:
            umur = int(input("Umur: "))
            if umur > 0:
                break
            print("Umur harus lebih dari 0!\n")
        except ValueError:
            print("Harap masukkan angka bulat untuk umur!\n")
            
    jenis_kelamin = input("Jenis Kelamin (L/P): ")
    return nama, umur, jenis_kelamin


def totalWaktuTidur():
    print("\n=== Kalkulator Waktu Tidur ===")
    
    # 1. Input & Validasi Jam Tidur
    while True:
        try:
            jam_t = int(input("Jam Anda tidur (0-23) --> "))
            menit_t = int(input("Menit Anda tidur (0-59) --> "))
            if 0 <= jam_t <= 23 and 0 <= menit_t <= 59:
                break
            print("Input tidak valid! Jam maksimal 23, menit maksimal 59.\n")
        except ValueError:
            print("Harap masukkan angka bulat!\n")

    # 2. Input & Validasi Jam Bangun
    while True:
        try:
            jam_b = int(input("Jam Anda bangun (0-23) --> "))
            menit_b = int(input("Menit Anda bangun (0-59) --> "))
            if 0 <= jam_b <= 23 and 0 <= menit_b <= 59:
                break
            print("Input tidak valid! Jam maksimal 23, menit maksimal 59.\n")
        except ValueError:
            print("Harap masukkan angka bulat!\n")

    # 3. Penentuan Format AM/PM
    format_tidur = "PM" if jam_t >= 12 else "AM"
    format_bangun = "PM" if jam_b >= 12 else "AM"

    # 4. Kalkulasi Total Menit dari jam 00:00
    total_menit_tidur = (jam_t * 60) + menit_t
    total_menit_bangun = (jam_b * 60) + menit_b

    # 5. Logika Durasi Tidur
    durasi_menit = total_menit_bangun - total_menit_tidur

    if durasi_menit < 0:
        durasi_menit += 24 * 60  

    durasi_jam = durasi_menit // 60
    sisa_menit = durasi_menit % 60

    # 6. Pembuatan String
    jam_tidur_str = f"{jam_t:02d}:{menit_t:02d} {format_tidur}"
    jam_bangun_str = f"{jam_b:02d}:{menit_b:02d} {format_bangun}"
    total_waktu_str = f"{durasi_jam} jam {sisa_menit} menit"

    # Return string untuk dicetak, DAN angka untuk dievaluasi kesehatannya
    return jam_tidur_str, jam_bangun_str, total_waktu_str, durasi_jam, sisa_menit


def dapatkan_rekomendasi_tidur(umur):
    """Menentukan rekomendasi jam tidur berdasarkan umur (Standar WHO/NSF)."""
    if umur <= 5:
        return 10, 14, "Balita"
    elif umur <= 12:
        return 9, 12, "Anak-anak"
    elif umur <= 18:
        return 8, 10, "Remaja"
    elif umur <= 64:
        return 7, 9, "Dewasa"
    else:
        return 7, 8, "Lansia"


def evaluasi_kesehatan(durasi_desimal, min_jam, max_jam):
    """Mengevaluasi durasi tidur dan memberikan dampak kesehatan."""
    if durasi_desimal < min_jam:
        status = "KURANG TIDUR (Sleep Deprivation)"
        dampak = "Penurunan daya ingat, daya tahan tubuh melemah, hormon stres meningkat."
    elif durasi_desimal > max_jam:
        status = "TIDUR BERLEBIH (Oversleeping)"
        dampak = "Meningkatkan risiko kelelahan kronis (lethargy), penurunan mood, dan masalah metabolisme."
    else:
        status = "OPTIMAL"
        dampak = "Pemulihan sel tubuh maksimal, fokus tajam, mood stabil, dan sistem imun berfungsi dengan baik."
        
    return status, dampak


# ==========================================
# FUNGSI UTAMA (Menjalankan semua alur program)
# ==========================================
def jalankan_aplikasi():
    # 1. Minta Biodata
    nama, umur, jenis_kelamin = inputBiodata()
    
    # 2. Hitung Waktu Tidur
    jam_tidur_str, jam_bangun_str, total_waktu_str, d_jam, d_menit = totalWaktuTidur()
    
    # 3. Proses Analisis Kesehatan
    durasi_desimal = d_jam + (d_menit / 60) # Ubah ke desimal (misal 7 jam 30 menit = 7.5)
    min_jam, max_jam, kategori_usia = dapatkan_rekomendasi_tidur(umur)
    status_tidur, dampak_kesehatan = evaluasi_kesehatan(durasi_desimal, min_jam, max_jam)
    
    # 4. Tampilkan Laporan Akhir
    print("\n" + "="*50)
    print("LAPORAN ANALISIS POLA TIDUR PASIEN")
    print("="*50)
    print(f"Nama Pasien     : {nama} ({jenis_kelamin.upper()})")
    print(f"Kategori Usia   : {kategori_usia} ({umur} tahun)")
    print("-" * 50)
    print(f"Waktu Tidur     : {jam_tidur_str}")
    print(f"Waktu Bangun    : {jam_bangun_str}")
    print(f"Durasi Aktual   : {total_waktu_str}")
    print(f"Rekomendasi WHO : {min_jam} - {max_jam} jam per malam")
    print("-" * 50)
    print(f"Status          : {status_tidur}")
    print(f"Dampak Medis    : {dampak_kesehatan}")
    print("="*50)

# Memulai Program
if __name__ == "__main__":
    jalankan_aplikasi()