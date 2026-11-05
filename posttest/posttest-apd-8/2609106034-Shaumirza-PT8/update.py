from menu import jarvis_tampilkan_daftar, jarvis_statusbaca

def ubah_status(library):
    if len(library) == 0:
        print("Belum ada manga di sini, nih~")
    else:
        jarvis_tampilkan_daftar(library, "Status")
        pilih_manga = input("Judul manga yang mau diubah statusnya: ")
        if pilih_manga in library:
            status_baru = jarvis_statusbaca()
            if status_baru != "":
                library[pilih_manga] = status_baru
                print("Yatta! Status manganya berhasil diubah~")
        else:
            print("Judulnya nggak ada, coba cek lagi yaa")
    input("ENTER ya buat balik!!")