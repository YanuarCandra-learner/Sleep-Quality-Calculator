if __name__ == "__main__":
    import main

import textwrap
import time

def pilihan_menu():
    #display menu
    print("\n=== Pilih Informasi ===")
    print("1. Tentang Kualitas Tidur")
    print("2. Tentang aplikasi")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    #validasi input 1,2,3
    while pilihan not in ["1", "2", "3"]:
        print("Pilihan tidak valid. Silahkan pilih 1, 2, atau 3.")
        pilihan = input("Masukkan pilihan (1/2/3): ")
    return pilihan

def jalankan_about():
    while True:
        pilihan = pilihan_menu()
        if pilihan == "1":
            header = print("\n", "=" * 50, f"Tentang Kualitas Tidur".center(50), "=" * 50, sep="\n")
            teks = "Kualitas tidur adalah ukuran seberapa baik seseorang tidur. " \
            "Faktor-faktor yang mempengaruhi kualitas tidur meliputi durasi tidur, kedalaman tidur, dan seberapa sering seseorang terbangun di malam hari. " \
            "Kualitas tidur yang baik penting untuk kesehatan fisik dan mental."
            hasil = textwrap.fill(teks, width=50)
            print(hasil)
        elif pilihan == "2":
            header = print("\n", "=" * 50, f"Tentang Aplikasi".center(50), "=" * 50, sep="\n")
            teks= "Aplikasi ini dirancang untuk membantu pengguna menghitung kualitas tidurnya berdasarkan jam tidur dan jam bangun. " \
            "Aplikasi ini juga memberikan informasi tentang durasi tidur yang direkomendasikan berdasarkan usia pengguna."
            hasil = textwrap.fill(teks, width=50)
            print(hasil)
        elif pilihan == "3":
            print("Kembali ke menu utama...")
            time.sleep(2)
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih 1, 2, atau 3.")

def credit():
    while True:
        
        print("\n", "=" * 50, f"Credit".center(50), "=" * 50, sep="\n")
        teks = f"YANUAR ADI CANDRA".center(50)
        link = f"https://github.com/YanuarCandra-learner".center(50)
        hasil = textwrap.fill(teks, width=50)
        linked = textwrap.fill(link, width=50)
        print(hasil)
        print(linked)
        input("\nTekan Enter untuk kembali ke menu utama...")
        break