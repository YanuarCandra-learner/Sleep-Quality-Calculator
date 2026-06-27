while True:
    import os
    import calculation
    import about

    os.system('cls' if os.name == 'nt' else 'clear')
    judulProgram = "SELAMAT DATANG DI PROGRAM SLEEP-QUALITY-CALCULATOR"
    p_judulProgram = len(judulProgram)
    #header program
    print("=" * p_judulProgram, judulProgram, "=" * p_judulProgram, sep="\n")
    print("FITUR PROGRAM : ")
    print(f"1. kalkulasi kualitas tidur")
    print(f"2. Informasi seputar tidur")
    print(f"3. Credit")
    print(f"4. Exit")

    #input menu
    menu = input("silahkan masukkan nomor menu : ")
    while not menu.isdigit():
        print("Gunakan angka untuk memilih menu.")
        menu = input("silahkan masukkan nomor menu : ")
        
    while menu.isdigit():
        menu = int(menu)
        match menu: #switch case untuk menu
            case 1:
                #menjalankan kalkulasi kualitas tidur PERTAMA KALI
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
                calculation.jalankan_aplikasi()
                #LOGIKA REPEAT 
                goto_main = input("\n\nApakah Anda ingin melakukan kalkulasi jam tidur lagi? (y/n): ")
                while goto_main.lower() == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    calculation.jalankan_aplikasi()
                    goto_main = input("\n\nApakah Anda ingin melakukan kalkulasi jam tidur lagi? (y/n): ") # Memanggil fungsi ini lagi untuk mengulang program
                else:
                    import main 
                break
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
                about.jalankan_about()
                break
            case 3:
                print("cek")
                # about.credit()
                break
            case 4:
                print("Terima kasih telah menggunakan program ini.")
                exit()
            case _:
                print("Pilih Angka Sesuai Dengan Urutan program diatas.")
                menu = input("silahkan masukkan nomor menu : ")
    
    
           