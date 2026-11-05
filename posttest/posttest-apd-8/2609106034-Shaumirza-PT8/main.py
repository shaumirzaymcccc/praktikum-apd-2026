from data import akun
from menu import menu_awal, menu_admin, menu_user
from daftarmasuk import loging, register
from create import tambah_katalog, tambah_library
from read import lihat_katalog, lihat_library
from update import ubah_status
from delete import hapus_katalog, hapus_library

kotayomi_menu = ""
while kotayomi_menu != "3":
    kotayomi_menu = menu_awal()

    if kotayomi_menu == "1":
        nama_aktif = loging()
        if nama_aktif != "":
            if akun[nama_aktif]["role"] == "admin":
                pilihan = ""
                while pilihan != "4":
                    pilihan = menu_admin(nama_aktif)
                    if pilihan == "1":
                        lihat_katalog()
                    elif pilihan == "2":
                        tambah_katalog()
                    elif pilihan == "3":
                        hapus_katalog()
                    elif pilihan == "4":
                        print("Berhasil logout, sampai jumpa lagi~")
                        input("ENTER ya buat balik!!")
                    else:
                        print("Ehh, pilihan itu nggak ada di menu!")
                        input("ENTER ya buat balik!!")
            else:
                library = akun[nama_aktif]["library"]
                pilihan = ""
                while pilihan != "5":
                    pilihan = menu_user(nama_aktif)

                    if pilihan == "1":
                        lihat_library(library)
                    elif pilihan == "2":
                        tambah_library(library)
                    elif pilihan == "3":
                        ubah_status(library)
                    elif pilihan == "4":
                        hapus_library(library)
                    elif pilihan == "5":
                        print("Berhasil logout, sampai jumpa lagi~")
                        input("ENTER ya buat balik!!")
                    else:
                        print("Ehh, pilihan itu nggak ada di menu!")
                        input("ENTER ya buat balik!!")

    elif kotayomi_menu == "2":
        register()

    elif kotayomi_menu == "3":
        print("Maaciw udah gunain Kotayomii! Sampai jumpa~")

    else:
        print("Ehh, pilih angka 1 sampai 3 ya!")
        input("ENTER dulu yaa buat balik~")