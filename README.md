<div align="center">

# 😴 Sleep Quality Calculator

### Analisis Pola Tidur & Evaluasi Kesehatan Berbasis CLI

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=for-the-badge)](#-persyaratan-sistem)

<br>

<p align="center">
  <strong>Aplikasi CLI Python yang menganalisis pola tidur pengguna berdasarkan durasi tidur aktual, kemudian memberikan evaluasi kesehatan dan rekomendasi sesuai standar WHO/NSF berdasarkan kategori usia.</strong>
</p>

---

[Fitur](#-fitur-utama) •
[Instalasi](#-instalasi) •
[Penggunaan](#-cara-penggunaan) •
[Struktur Proyek](#-struktur-proyek) •
[Kontribusi](#-kontribusi)

</div>

<br>

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Instalasi](#-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Struktur Proyek](#-struktur-proyek)
- [Penjelasan Modul](#-penjelasan-modul)
- [Standar Rekomendasi Tidur](#-standar-rekomendasi-tidur-whonsf)
- [Kontribusi](#-kontribusi)

---

## 🔍 Tentang Proyek

**Sleep Quality Calculator** adalah aplikasi berbasis Command Line Interface (CLI) yang dibangun menggunakan Python. Aplikasi ini dirancang untuk membantu pengguna menganalisis kualitas tidurnya secara cepat dan akurat.

Pengguna cukup memasukkan biodata sederhana (nama, umur, jenis kelamin) beserta jam tidur dan jam bangun, lalu aplikasi akan secara otomatis:

1. Menghitung **durasi tidur aktual**
2. Menentukan **kategori usia** pengguna
3. Membandingkan durasi tidur dengan **rekomendasi WHO/NSF**
4. Memberikan **status evaluasi** dan **dampak medis** yang relevan

---

## ✨ Fitur Utama

### 🧮 Kalkulasi Kualitas Tidur
- Input jam tidur dan jam bangun dengan format **jam & menit** (mendukung format 24 jam)
- Kalkulasi otomatis durasi tidur, termasuk logika **tidur melewati tengah malam**
- Evaluasi status tidur: `OPTIMAL`, `KURANG TIDUR`, `SANGAT KURANG TIDUR`, atau `TIDUR BERLEBIH`
- Dampak medis yang disesuaikan berdasarkan **kategori usia** pengguna

### 📊 Laporan Analisis Lengkap
- Laporan terformat rapi yang menampilkan:
  - Identitas pasien (nama & jenis kelamin)
  - Kategori usia berdasarkan umur
  - Waktu tidur & bangun
  - Durasi aktual vs rekomendasi WHO
  - Status evaluasi & dampak medis

### 📚 Informasi Seputar Tidur
- Penjelasan mengenai **apa itu kualitas tidur** dan faktor-faktor yang mempengaruhinya
- Informasi **tentang aplikasi** dan bagaimana cara kerjanya
- Disajikan dalam format teks yang rapi menggunakan `textwrap`

### 🔒 Validasi Input yang Ketat
- Nama hanya menerima **huruf alfabet** dan tidak boleh kosong
- Umur harus berupa **angka bulat positif**
- Jenis kelamin hanya menerima **`L`** atau **`P`**
- Jam & menit divalidasi sesuai rentang **0–23** dan **0–59**
- Menu hanya menerima input angka yang sesuai

### 🔄 Fitur Repeat & Navigasi
- Setelah kalkulasi, pengguna dapat **mengulang kalkulasi** tanpa kembali ke menu utama
- Navigasi antar menu yang intuitif dengan sistem **match-case**
- Layar otomatis dibersihkan (`cls`/`clear`) untuk pengalaman pengguna yang bersih

---

## 💻 Persyaratan Sistem

| Komponen | Minimum |
|----------|---------|
| **Python** | 3.10 atau lebih baru (diperlukan untuk `match-case`) |
| **OS** | Windows, Linux, atau macOS |
| **Dependensi Eksternal** | Tidak ada — hanya menggunakan library bawaan Python |

> [!NOTE]
> Aplikasi ini menggunakan syntax `match-case` yang diperkenalkan di **Python 3.10**. Pastikan versi Python Anda mendukung fitur ini.

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/YanuarCandra-learner/Sleep-Quality-Calculator.git
cd Sleep-Quality-Calculator
```

### 2. Pastikan Python Terinstal

```bash
python --version
```

> Pastikan output menunjukkan versi **3.10** atau lebih baru.

### 3. Jalankan Aplikasi

```bash
python main.py
```

> [!TIP]
> Tidak diperlukan instalasi dependensi tambahan. Aplikasi ini sepenuhnya menggunakan library bawaan Python (`os`, `time`, `textwrap`).

---

## 📖 Cara Penggunaan

### Menu Utama

Saat aplikasi dijalankan, pengguna akan disambut dengan menu utama:

```
==================================================
   SELAMAT DATANG DI PROGRAM SLEEP-QUALITY-CALCULATOR
==================================================
FITUR PROGRAM :
1. Kalkulasi kualitas tidur
2. Informasi seputar tidur
3. Credit
4. Exit
```

### Alur Kalkulasi Kualitas Tidur (Menu 1)

```
📝 Langkah 1 — Masukkan Biodata
   ├── Nama
   ├── Umur
   └── Jenis Kelamin (L/P)

⏰ Langkah 2 — Masukkan Waktu Tidur
   ├── Jam & Menit tidur
   └── Jam & Menit bangun

📊 Langkah 3 — Analisis Otomatis
   └── Sistem memproses data Anda...

📋 Langkah 4 — Laporan Akhir
```

### Contoh Output Laporan

```
=====================================================================================
                         LAPORAN ANALISIS POLA TIDUR ANDA
=====================================================================================
Nama Pasien     : Budi (L)
Kategori Usia   : Dewasa (25 tahun)
-------------------------------------------------------------------------------------
Waktu Tidur     : 23:30
Waktu Bangun    : 06:00
Durasi Aktual   : 6 jam 30 menit
Rekomendasi WHO : 7 - 9 jam per malam
-------------------------------------------------------------------------------------
Status          : KURANG TIDUR
Dampak Medis    : Mudah lelah, mood swing, dan penurunan konsentrasi.
=====================================================================================
```

### Alur Informasi Seputar Tidur (Menu 2)

```
=== Pilih Informasi ===
1. Tentang Kualitas Tidur
2. Tentang Aplikasi
3. Keluar
```

---

## 📂 Struktur Proyek

```
Sleep-Quality-Calculator/
│
├── main.py              # Entry point — Menu utama & navigasi program
├── calculation.py       # Modul kalkulasi — Logika inti analisis kualitas tidur
├── about.py             # Modul informasi — Edukasi seputar tidur, tentang aplikasi & credit
└── README.md            # Dokumentasi proyek
```

---

## 🧩 Penjelasan Modul

### `main.py` — Entry Point

> **File utama yang menjalankan seluruh program.**

| Tanggung Jawab | Deskripsi |
|-----------------|-----------|
| Menu Utama | Menampilkan daftar fitur program dan menerima input pengguna |
| Routing | Mengarahkan pengguna ke modul yang sesuai menggunakan `match-case` |
| Repeat Logic | Menyediakan opsi untuk mengulang kalkulasi tanpa restart |
| Screen Clear | Membersihkan layar terminal untuk UX yang lebih baik |

**Fungsi yang digunakan:**
- `calculation.jalankan_aplikasi()` — Menjalankan kalkulasi kualitas tidur
- `about.jalankan_about()` — Menampilkan informasi seputar tidur
- `about.credit()` — Menampilkan informasi kredit pembuat aplikasi

---

### `calculation.py` — Logika Inti Kalkulasi

> **Modul yang menangani seluruh proses kalkulasi dan evaluasi kualitas tidur.**

| Fungsi | Deskripsi |
|--------|-----------|
| `inputBiodata()` | Mengumpulkan dan memvalidasi nama, umur, dan jenis kelamin pengguna |
| `totalWaktuTidur()` | Menghitung durasi tidur berdasarkan jam tidur & bangun (mendukung lintas tengah malam) |
| `dapatkan_rekomendasi_tidur(umur)` | Menentukan rekomendasi durasi tidur sesuai standar WHO/NSF berdasarkan umur |
| `evaluasi_kesehatan(durasi, kategori)` | Mengevaluasi status tidur dan dampak medis berdasarkan durasi aktual & kategori usia |
| `jalankan_aplikasi()` | Fungsi utama yang mengorkestrasi seluruh alur kalkulasi hingga laporan akhir |

**Logika khusus:**
- Durasi tidur dihitung dalam **menit** lalu dikonversi ke format jam & menit
- Jika durasi negatif (tidur melewati tengah malam), otomatis ditambah **1440 menit** (24 jam)
- Durasi dikonversi ke **desimal** (contoh: 7 jam 30 menit → 7.5) untuk evaluasi kesehatan

---

### `about.py` — Modul Informasi & Credit

> **Modul yang menyimpan dan menampilkan informasi edukatif seputar kualitas tidur serta informasi kredit pembuat.**

| Fungsi | Deskripsi |
|--------|-----------||
| `pilihan_menu()` | Menampilkan submenu informasi dan memvalidasi input pengguna |
| `jalankan_about()` | Menjalankan loop interaktif untuk menampilkan informasi yang dipilih |
| `credit()` | Menampilkan informasi kredit pembuat aplikasi beserta tautan GitHub |

**Konten informasi:**
- **Tentang Kualitas Tidur** — Penjelasan mengenai definisi kualitas tidur, faktor-faktor yang mempengaruhi (durasi, kedalaman, frekuensi terbangun), dan pentingnya bagi kesehatan
- **Tentang Aplikasi** — Deskripsi tujuan dan cara kerja aplikasi
- **Credit** — Menampilkan nama pembuat dan tautan profil GitHub

---

## 🏥 Standar Rekomendasi Tidur (WHO/NSF)

Aplikasi ini menggunakan standar rekomendasi dari **World Health Organization (WHO)** dan **National Sleep Foundation (NSF)** untuk mengevaluasi kualitas tidur:

| Kategori Usia | Rentang Umur | Rekomendasi Tidur |
|---------------|:------------:|:-----------------:|
| 👶 Balita | ≤ 5 tahun | 11 – 14 jam |
| 🧒 Anak-anak | 6 – 13 tahun | 9 – 12 jam |
| 🧑 Remaja | 14 – 17 tahun | 8 – 10 jam |
| 👨 Dewasa | 18 – 64 tahun | 7 – 9 jam |
| 🧓 Lansia | ≥ 65 tahun | 7 – 8 jam |

### Status Evaluasi

| Status | Makna |
|--------|-------|
| 🟢 `OPTIMAL` | Durasi tidur sesuai rekomendasi — kondisi kesehatan terjaga |
| 🟡 `KURANG TIDUR` | Durasi tidur di bawah rekomendasi — berpotensi gangguan ringan |
| 🔴 `SANGAT KURANG TIDUR` | Durasi tidur jauh di bawah rekomendasi — risiko kesehatan serius |
| 🟠 `TIDUR BERLEBIH` | Durasi tidur melebihi rekomendasi — berpotensi gangguan metabolisme |

---

## 🛠️ Tech Stack

| Teknologi | Penggunaan |
|-----------|------------|
| **Python 3.10+** | Bahasa pemrograman utama |
| `os` | Membersihkan layar terminal (cross-platform) |
| `time` | Simulasi loading saat proses analisis |
| `textwrap` | Memformat teks informasi agar rapi di terminal |

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi:

1. **Fork** repository ini
2. Buat **branch** baru (`git checkout -b feature/FiturBaru`)
3. **Commit** perubahan Anda (`git commit -m "Menambahkan fitur baru"`)
4. **Push** ke branch (`git push origin feature/FiturBaru`)
5. Buat **Pull Request**

> [!IMPORTANT]
> Pastikan kode Anda telah diuji dan mengikuti konvensi penamaan yang konsisten dengan proyek ini.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE) — Anda bebas menggunakan, memodifikasi, dan mendistribusikan proyek ini.

---

<div align="center">

**Dibuat dengan ❤️ menggunakan Python**

⭐ *Jangan lupa berikan star jika proyek ini bermanfaat!* ⭐

</div>
