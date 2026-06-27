while True:
    import calculation
    import about
    
    judulProgram = "SELAMAT DATANG DI PROGRAM SLEEP-QUALITY-CALCULATOR"
    p_judulProgram = len(judulProgram)
    #header program
    print("=" * p_judulProgram, judulProgram, "=" * p_judulProgram, sep="\n")
    print("FITUR PROGRAM : ")
    print(f"1. kalkulasi kualitas tidur")
    print(f"2. Informasi seputar tidur")
    print(f"3. Credit")
    print(f"4. Exit")


    menu = input("silahkan masukkan nomor menu : ")
    while not menu.isdigit():
        print("Gunakan angka untuk memilih menu.")
        menu = input("silahkan masukkan nomor menu : ")
        

    while menu.isdigit():
        menu = int(menu)
        match menu:
            case 1:
                calculation.jalankan_aplikasi()
                break
            case 2:
                print("cek")
                
                print("fungsi ini akan segera hadir, stay tune untuk update selanjutnya")
                # about.about()
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
    
    
           