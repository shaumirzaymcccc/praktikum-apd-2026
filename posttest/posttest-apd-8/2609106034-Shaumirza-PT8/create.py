from data import katalog_rawr
from menu import jarvis_tampilkan_daftar, jarvis_statusbaca

def tambah_katalog():
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

def tambah_library(library):
    if len(katalog_rawr) == 0:
        print("Katalog masih kosong, tunggu admin nambahin ya~")
    else:
        jarvis_tampilkan_daftar(katalog_rawr, "Genre")
        tambah_manga = input("Judul manga yang mau ditambah: ")
        if tambah_manga not in katalog_rawr:
            print("Judulnya nggak ada di katalog, coba cek lagi yaa")
        elif tambah_manga in library:
            print("Manga itu udah ada di library kamu~")
        else:
            status_dipilih = jarvis_statusbaca()
            if status_dipilih != "":
                library[tambah_manga] = status_dipilih
                print(f"Yatta! '{tambah_manga}' berhasil ditambahkan~")
    input("ENTER ya buat balik!!")