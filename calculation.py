if __name__ == "__main__":
    import main

def inputBiodata():
    print("=== Masukkan Biodata Anda ===")
    nama = input("Nama: ")
    while len(nama) == 0:
        print("Nama tidak boleh kosong!")
        nama = input("Nama: ")
    while not nama.isalpha():
        print("Nama hanya boleh mengandung huruf!")
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
    while jenis_kelamin.upper() not in ["L", "P"]:
        print("'L' untuk Laki-laki atau 'P' untuk Perempuan.")
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
    jam_tidur_str = f"{jam_t:02d}:{menit_t:02d} "
    jam_bangun_str = f"{jam_b:02d}:{menit_b:02d} "
    total_waktu_str = f"{durasi_jam} jam {sisa_menit} menit"

    # Return string untuk dicetak, DAN angka untuk dievaluasi kesehatannya
    return jam_tidur_str, jam_bangun_str, total_waktu_str, durasi_jam, sisa_menit


def dapatkan_rekomendasi_tidur(umur):
    """Menentukan rekomendasi jam tidur berdasarkan umur (Standar WHO/NSF)."""
    if umur <= 5:
        return 11, 14, "Balita"
    elif umur <= 13:
        return 9, 12, "Anak-anak"
    elif umur <= 17:
        return 8, 10, "Remaja"
    elif umur <= 64:
        return 7, 9, "Dewasa"
    else:
        return 7, 8, "Lansia"


def evaluasi_kesehatan(durasi_desimal, kategori_usia):
    """PENJELASAN STATUS DAN DAMPAK BERDASARKAN KATEGORI UMUR"""
    if kategori_usia == "Balita":
        if durasi_desimal <  8:
            status = "SANGAT KURANG TIDUR"
            dampak = "Menghambat proses pertumbuhan dan menurunkan daya tahan tubuh."
        elif durasi_desimal >= 8 and durasi_desimal < 10:
            status = "KURANG TIDUR"
            dampak = "Menyebabkan anak mudah rewel, dan penurunan fokus saat belajar."
        elif durasi_desimal >= 15:
            status = "TIDUR BERLEBIH"
            dampak = "Menyebabkan anak tampak lesu, kurang aktif, dan gangguan metabolisme."
        else:
            status = "OPTIMAL"
            dampak = "Pertumbuhan optimal, daya tahan tubuh baik, dan perkembangan kognitif maksimal."
    if kategori_usia == "Anak-anak":
        if durasi_desimal <  7:
            status = "SANGAT KURANG TIDUR"
            dampak = "Daya tahan tubuh brekurang drastis dan gangguan metabolisme."
        elif durasi_desimal >= 7 and durasi_desimal < 9:
            status = "KURANG TIDUR"
            dampak = "Konsetrasi menurun, kemampuan mengingat menjadi terganggu."
        elif durasi_desimal >= 12:
            status = "TIDUR BERLEBIH"
            dampak = "Sleep Inertia (terasa berat dan pusing ketika bangun tidur)."
        else:
            status = "OPTIMAL"
            dampak = "Suasana hati terjaga, fokus belajar meningkat, dan sistem imun berfungsi baik."
    if kategori_usia == "Remaja":
        if durasi_desimal < 6:
            status = "SANGAT KURANG TIDUR"
            dampak = "Daya tahan tubuh menurun drastis, Jerawat semakin banyak, dan mood swing."
        elif durasi_desimal >= 6 and durasi_desimal < 8:
            status = "KURANG TIDUR"
            dampak = "Mood swing, serta sering menguap karena rasa kantuk akibat kurang tidur."
        elif durasi_desimal > 10:
            status = "TIDUR BERLEBIH"
            dampak = "Mudah lelah, dan gangguan metabolisme serta mengalami Sleep Inertia."
        else:
            status = "OPTIMAL"
            dampak = "Mood stabil, fokus belajar meningkat, dan sistem imun berfungsi baik."
    if kategori_usia == "Dewasa":
        if durasi_desimal < 5:
            status = "SANGAT KURANG TIDUR"
            dampak = "Daya tahan tubuh menurun drastis, mudah sakit, dan gangguan metabolisme."
        elif durasi_desimal >= 5 and durasi_desimal < 7:
            status = "KURANG TIDUR"
            dampak = "Mudah lelah, mood swing, dan penurunan konsentrasi."
        elif durasi_desimal > 9:
            status = "TIDUR BERLEBIH"
            dampak = "Lemas dan tidak bertenaga, serta meningkatkan resiko penyakit jantung."
        else:
            status = "OPTIMAL"
            dampak = "Regenerasi tubuh maksimal, fokus dan produktivitas meningkat."
    if kategori_usia == "Lansia":
        if durasi_desimal < 5:
            status = "SANGAT KURANG TIDUR"
            dampak = "Fungsi Kognitif berkurang, beresiko kecelakaan akibat gangguan keseimbangan."
        elif durasi_desimal >= 5 and durasi_desimal < 7:
            status = "KURANG TIDUR"
            dampak = "Daya Ingat menurun, mudah lelah, dan resiko hipertensi."
        elif durasi_desimal > 9:
            status = "TIDUR BERLEBIH"
            dampak = "Otot dan sendi rawan terjadi kekakuan."
        else:
            status = "OPTIMAL"
            dampak = "Kemampuan memori terjaga, serta meningkatkan sistem imun tubuh."    
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
    status_tidur, dampak_kesehatan = evaluasi_kesehatan(durasi_desimal, kategori_usia)
    
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
    goto_main = input("Apakah Anda ingin melakukan kalkulasi jam tidur lagi? (y/n): ")
    if goto_main.lower() == 'y':
        jalankan_aplikasi() # Memanggil fungsi ini lagi untuk mengulang program
    else:
        import main 

