from data import katalog_rawr
from menu import jarvis_tampilkan_daftar

def lihat_katalog():
    if len(katalog_rawr) == 0:
        print("Belum ada manga di katalog, nih~")
    else:
        jarvis_tampilkan_daftar(katalog_rawr, "Genre")
    input("ENTER ya buat balik!!")

def lihat_library(library):
    if len(library) == 0:
        print("Belum ada manga di sini, nih~")
    else:
        jarvis_tampilkan_daftar(library, "Status")
    input("ENTER ya buat balik!!")