# 1. Validasi login

nama_valid = "ezra"
pass_valid = "034"
masuk = False
for i in range(1, 4):
    print("============================")
    print("           Login            ")
    input_nama = input("Masukkan Nama: ")
    input_pass = input("Masukkan Password: ")
    print("============================")
 
    if nama_valid == input_nama and pass_valid == input_pass:
        masuk = True
        print("login berhasil")
        break
    else:
        print("username atau password salah")
        print(f"sisa kesempatan: {3 - i}")
if masuk == False:
    print("kesempatan login habis. program tidak bisa di akses sementara")
else:
    data_siswa = []
    kelas_daftar = []
 
    ulang = "iya"
    while ulang == "iya":

# 2. Input data siswa

        print("============================")
        print("      Input Data Siswa      ")
        nama = input("Masukkan Nama: ")

# Kelas harus ditulis konsisten contoh kyk A1 am a1 bisa jadi beda kelas. soalnya gtw ini boleh pake .lower apa engga
        kelas = input("Masukkan Kelas: ")

# Jawaban harus persis iya atau tidak (sama aja ini wkwk)
        kehadiran = input("ikut ujian (iya/tidak)? ")
        print("============================")

# 3. Nilai ujian
        if kehadiran == "iya":
            benar = int(input("Soal benar: "))
            salah = int(input("Soal salah: "))
            skor = benar * 5
            ikut = "ikut ujian"
        else:
            skor = 0
            ikut = "tidak ikut ujian"
            print("Nilai otomatis 0, tidak mengikuti ujian")
 
        data_siswa.append([nama, kelas, ikut, skor])

        sudah = False
        for i in kelas_daftar:
            if i == kelas:
                sudah = True
        if sudah == False:
            kelas_daftar.append(kelas)

# 4. Tanya apakah masih ingin menginput 

# Jawaban harus persis "iya" supaya lanjut, soalnya klo Iya, iYa, iyA, IYA porgram berhenti(sama aja sih wkwk)

        ulang = input("apakah anda masih ingin input data (iya/tidak)?")

# 5. Output data siswa (dibedakan per kelas, nested for)

    print("============================")
    print("      Hasil Nilai Siswa     ")
    print("============================")
    for berkelas in kelas_daftar:
        print(f"kelas {berkelas}")
        for WAWAWAWA in data_siswa:
            if WAWAWAWA[1] == berkelas:
                if WAWAWAWA[3] >= 80:
                    kategori = "Sangat baik"
                elif WAWAWAWA[3] >= 60:
                    kategori = "Baik"
                elif WAWAWAWA[3] >= 40:
                    kategori = "Cukup"
                else:
                    kategori = "Perlu belajar lagi"
                print(f"nama       : {WAWAWAWA[0]}")
                print(f"ikut ujian : {WAWAWAWA[2]}")
                print(f"nilai      : {WAWAWAWA[3]} ({kategori})")
                print("============================")