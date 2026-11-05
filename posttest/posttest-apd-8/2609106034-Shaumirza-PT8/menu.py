import os
from prettytable import PrettyTable
from data import status

def jarvis_tampilkan_menu(judul, isi_menu):
    tabel_menu = PrettyTable()
    tabel_menu.field_names = [judul]
    tabel_menu.align[judul] = "l"
    for baris in isi_menu:
        tabel_menu.add_row([baris])
    print(tabel_menu)

def menu_awal():
    os.system('cls' if os.name == 'nt' else 'clear')
    jarvis_tampilkan_menu("KOTAYOMI - SISTEM TRACKING MANGA", [
        "1. Login",
        "2. Register",
        "3. Keluar"])
    return input("Pilih (1-3): ")

def menu_admin(nama_aktif):
    os.system('cls' if os.name == 'nt' else 'clear')
    jarvis_tampilkan_menu(f"KOTAYOMI MENU - {nama_aktif} (admin)", [
        "1. Lihat katalog",
        "2. Tambah manga ke katalog",
        "3. Hapus manga dari katalog",
        "4. Keluar"])
    return input("Pilih menu (1-4): ")

def menu_user(nama_aktif):
    os.system('cls' if os.name == 'nt' else 'clear')
    jarvis_tampilkan_menu(f"KOTAYOMI MENU - {nama_aktif} (user)", [
        "1. Lihat Library",
        "2. Tambah manga dari katalog",
        "3. Update status manga",
        "4. Hapus manga dari library",
        "5. Keluar"])
    return input("Pilih menu (1-5): ")

def jarvis_tampilkan_daftar(daftar, nama_kolom):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Judul", nama_kolom]
    tabel.align["Judul"] = "l"
    tabel.align[nama_kolom] = "l"
    nomor = 1
    for manga in daftar:
        tabel.add_row([nomor, manga, daftar[manga]])
        nomor += 1
    print(tabel)

def jarvis_statusbaca():
    tabel_status = PrettyTable()
    tabel_status.field_names = ["No", "Status"]
    tabel_status.align["Status"] = "l"
    for BLEEOD in status:
        tabel_status.add_row([BLEEOD, status[BLEEOD]])
    print(tabel_status)
    pilih_status = input("Pilih status (1-3): ")
    try:
        return status[pilih_status]
    except KeyError:
        print("Ehh, pilih status 1 sampai 3 ya!")
        return ""