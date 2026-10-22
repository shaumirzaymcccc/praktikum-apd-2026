import os
status = {"1": "belum dibaca", "2": "sedang dibaca", "3": "selesai"}
akun = {
    "ezra": {"password": "67", "role": "admin", "library": {}},
    "zaidanoomfie": {"password": "67", "role": "user", "library": {}}}
katalog_rawr = {}

kotayomi_menu = ""
while kotayomi_menu != "3":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    print(" SELAMAT DATANG DI KOTAYOMI ")
    print("   SISTEM TRACKING MANGA    ")
    print("============================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    kotayomi_menu = input("Pilih (1-3): ")

    if kotayomi_menu == "1":
        login_nama = input("Masukkan Nama: ")
        login_password = input("Masukkan Password: ")
        masuk = False

        for telaviv in akun:
            if telaviv == login_nama and akun[telaviv]["password"] == login_password:
                masuk = True
                nama_aktif = telaviv
                akun_aktif = akun[telaviv]
                break

        if masuk:
            library = akun_aktif["library"]
            role = akun_aktif["role"]
            pilihan = ""

            while pilihan != "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============================")
                print("        KOTAYOMI MENU")
                print(f"        {nama_aktif} ({role})")
                print("============================")

                if role == "admin":
                    print("1. Lihat katalog")
                    print("2. Tambah manga ke katalog")
                    print("3. Hapus manga dari katalog")
                    print("4. Keluar")
                    pilihan = input("Pilih menu (1-4): ")
                else:
                    print("1. Lihat Library")
                    print("2. Tambah manga dari katalog")
                    print("3. Update status manga")
                    print("4. Hapus manga dari library")
                    print("5. Keluar")
                    pilihan = input("Pilih menu (1-5): ")

                if pilihan == "1" and role == "admin":
                    if len(katalog_rawr) == 0:
                        print("Belum ada manga di katalog, nih~")
                    else:
                        nomor = 1
                        for manga in katalog_rawr:
                            print(f"{nomor}. {manga} - {katalog_rawr[manga]}")
                            nomor += 1
                    input("ENTER ya buat balik!!")

                elif pilihan == "2" and role == "admin":
                    tambah_manga = input("Judul manga: ")
                    genre = input("Genre: ")
                    if tambah_manga == "" or genre == "":
                        print("Judul dan genre jangan kosong dongg >_<")
                    elif tambah_manga in katalog_rawr:
                        print("Manga itu udah ada di katalog~")
                    else:
                        katalog_rawr[tambah_manga] = genre
                        print(f"Yatta! '{tambah_manga}' berhasil ditambahkan ke katalog~")
                    input("ENTER ya buat balik!!")

                elif pilihan == "3" and role == "admin":
                    if len(katalog_rawr) == 0:
                        print("Belum ada manga di katalog, nih~")
                    else:
                        nomor = 1
                        for manga in katalog_rawr:
                            print(f"{nomor}. {manga} - {katalog_rawr[manga]}")
                            nomor += 1

                        hapusmanga = input("Judul manga yang mau dihapus: ")
                        if hapusmanga in katalog_rawr:
                            del katalog_rawr[hapusmanga]
                            for EBKEBKEBK in akun:
                                if hapusmanga in akun[EBKEBKEBK]["library"]:
                                    del akun[EBKEBKEBK]["library"][hapusmanga]
                            print(f"Bye-bye, '{hapusmanga}', berhasil dihapus~")
                        else:
                            print("Judulnya nggak ada, coba cek lagi yaa")
                    input("ENTER ya buat balik!!")

                elif pilihan == "4" and role == "admin":
                    print("Berhasil logout, sampai jumpa lagi~")
                    pilihan = "5"
                    input("ENTER ya buat balik!!")

                elif pilihan == "1":
                    if len(library) == 0:
                        print("Belum ada manga di sini, nih~")
                    else:
                        nomor = 1
                        for manga in library:
                            print(f"{nomor}. {manga} - {library[manga]}")
                            nomor += 1
                    input("ENTER ya buat balik!!")

                elif pilihan == "2":
                    if len(katalog_rawr) == 0:
                        print("Katalog masih kosong, tunggu admin nambahin ya~")
                    else:
                        nomor = 1
                        for manga in katalog_rawr:
                            print(f"{nomor}. {manga} - {katalog_rawr[manga]}")
                            nomor += 1

                        tambah_manga = input("Judul manga yang mau ditambah: ")
                        if tambah_manga not in katalog_rawr:
                            print("Judulnya nggak ada di katalog, coba cek lagi yaa")
                        elif tambah_manga in library:
                            print("Manga itu udah ada di library kamu~")
                        else:
                            for BLEEOD in status:
                                print(f"{BLEEOD}. {status[BLEEOD]}")

                            pilih_status = input("Pilih status (1-3): ")
                            if pilih_status in status:
                                library[tambah_manga] = status[pilih_status]
                                print(f"Yatta! '{tambah_manga}' berhasil ditambahkan~")
                            else:
                                print("Ehh, pilih status 1 sampai 3 ya!")
                    input("ENTER ya buat balik!!")

                elif pilihan == "3":
                    if len(library) == 0:
                        print("Belum ada manga di sini, nih~")
                    else:
                        nomor = 1
                        for manga in library:
                            print(f"{nomor}. {manga} - {library[manga]}")
                            nomor += 1

                        pilih_manga = input("Judul manga yang mau diubah: ")
                        if pilih_manga in library:
                            for AWAWAWAW in status:
                                print(f"{AWAWAWAW}. {status[AWAWAWAW]}")

                            pilih_status = input("Pilih status baru (1-3): ")
                            if pilih_status in status:
                                library[pilih_manga] = status[pilih_status]
                                print("Yatta! Status manganya berhasil diubah~")
                            else:
                                print("Ehh, pilih status 1 sampai 3 ya!")
                        else:
                            print("Judulnya nggak ada, coba cek lagi yaa")
                    input("ENTER ya buat balik!!")

                elif pilihan == "4":
                    if len(library) == 0:
                        print("Belum ada manga di sini, nih~")
                    else:
                        nomor = 1
                        for manga in library:
                            print(f"{nomor}. {manga} - {library[manga]}")
                            nomor += 1

                        hapus_manga = input("Judul manga yang mau dihapus: ")
                        if hapus_manga in library:
                            del library[hapus_manga]
                            print(f"Bye-bye, '{hapus_manga}', berhasil dihapus~")
                        else:
                            print("Judulnya nggak ada, coba cek lagi yaa")
                    input("ENTER ya buat balik!!")

                elif pilihan == "5":
                    print("Berhasil logout, sampai jumpa lagi~")
                    input("ENTER ya buat balik!!")

                else:
                    print("Ehh, pilihan itu nggak ada di menu!")
                    input("ENTER ya buat balik!!")
        else:
            print("Yahh, nama atau password-nya salah T-T")
            input("ENTER dulu yaa buat balik~")

    elif kotayomi_menu == "2":
        nama_baru = input("Masukkan Nama Baru: ")
        pass_baru = input("Masukkan Password Baru: ")
        sudah = False

        for gatau in akun:
            if gatau == nama_baru:
                sudah = True
                break

        if nama_baru == "" or pass_baru == "":
            print("Nama dan password jangan dikosongin ya!")
        elif sudah:
            print("Nama itu udah dipakai, cari nama lain yaa")
        else:
            akun[nama_baru] = {"password": pass_baru, "role": "user", "library": {}}
            print(f"Akun '{nama_baru}' berhasil dibuat! Yoroshiku~")
        input("ENTER dulu yaa buat balik~")

    elif kotayomi_menu == "3":
        print("Maaciw udah gunain Kotayomii! Sampai jumpa~")

    else:
        print("Ehh, pilih angka 1 sampai 3 ya!")
        input("ENTER dulu yaa buat balik~")