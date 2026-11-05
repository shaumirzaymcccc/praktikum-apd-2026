from data import akun, katalog_rawr
from menu import jarvis_tampilkan_daftar

def jarvis_hapus_atmint(judul):
    for EBKEBKEBK in akun:
        if judul in akun[EBKEBKEBK]["library"]:
            del akun[EBKEBKEBK]["library"][judul]

def hapus_katalog():
    if len(katalog_rawr) == 0:
        print("Belum ada manga di katalog, nih~")
    else:
        jarvis_tampilkan_daftar(katalog_rawr, "Genre")
        hapusmanga = input("Judul manga yang mau dihapus: ")
        try:
            del katalog_rawr[hapusmanga]
            jarvis_hapus_atmint(hapusmanga)
            print(f"Bye-bye, '{hapusmanga}', berhasil dihapus~")
        except KeyError:
            print("Judulnya nggak ada, coba cek lagi yaa")
    input("ENTER ya buat balik!!")

def hapus_library(library):
    if len(library) == 0:
        print("Belum ada manga di sini, nih~")
    else:
        jarvis_tampilkan_daftar(library, "Status")
        hapus_manga = input("Judul manga yang mau dihapus: ")
        try:
            del library[hapus_manga]
            print(f"Bye-bye, '{hapus_manga}', berhasil dihapus~")
        except KeyError:
            print("Judulnya nggak ada, coba cek lagi yaa")
    input("ENTER ya buat balik!!")