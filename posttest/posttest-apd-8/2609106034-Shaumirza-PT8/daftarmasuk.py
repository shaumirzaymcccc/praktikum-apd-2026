from data import akun

def cek_login(nama, password):
    for i in akun:
        if i == nama and akun[i]["password"] == password:
            return True
    return False

def nama_sudah_dipakai(nama):
    for gatau in akun:
        if gatau == nama:
            return True
    return False

def loging():
    login_nama = input("Masukkan Nama: ")
    login_password = input("Masukkan Password: ")

    if cek_login(login_nama, login_password):
        return login_nama
    else:
        print("Yahh, nama atau password-nya salah T-T")
        input("ENTER dulu yaa buat balik~")
        return ""

def register():
    nama_baru = input("Masukkan Nama Baru: ")
    pass_baru = input("Masukkan Password Baru: ")

    if nama_baru == "" or pass_baru == "":
        print("Nama dan password jangan dikosongin ya!")
    elif nama_sudah_dipakai(nama_baru):
        print("Nama itu udah dipakai, cari nama lain yaa")
    else:
        akun[nama_baru] = {"password": pass_baru, "role": "user", "library": {}}
        print(f"Akun '{nama_baru}' berhasil dibuat! Yoroshiku~")
    input("ENTER dulu yaa buat balik~")