# 1. Validasi login
nama_panggilan = "ezra"
nim = "34"

print("==================================")
print("      SELAMAT DATANG DI SPBU      ")
print("==================================")
nama_masuk = input("masukkan nama: ")
nim_masuk = input("masukkan 2 digit terakhir nim: ")

# 2. Pilihan Jenis BBM
if nama_masuk == nama_panggilan and nim_masuk == nim:
    print("Login berhasil, Selamat berbelanja")
    
    print("==================================")
    print("        PILIHAN JENIS BBM         ") 
    print("==================================")
    print("Pertalite: Rp. 10.000             ")
    print("Pertamax: Rp. 12.500              ")
    print("Pertamax Turbo: Rp. 15.000        ")
    print("==================================")
    
    pilihan = int(input("Pilih jenis BBM(1-3): "))
    liter = int(input("Pilih jumlah liter: "))
    
    if pilihan == 1:
        jenis = "pertalite"
        harga = 10000
    elif pilihan == 2:
        jenis = "pertamax"
        harga = 12500
    elif pilihan == 3:
        jenis = "pertamax turbo"
        harga = 15000
    else:
        jenis = "ga di ketahui"
        harga = 0


# 3. Ketentuan Diskon
    if liter >= 10:
        persen_diskon = 0.1
    elif liter >= 5:
        persen_diskon = 0.05
    else:
        persen_diskon = 0

# 4. Rumus
    total_harga = harga * liter
    diskon = persen_diskon * total_harga
    total_bayar = total_harga - diskon

# POIN PLUS (+)
    member = input("apakah anda member SPBU?(iya/tidak): ")

    if member == "iya":
        diskon_member = 0.02 * total_harga
        keterangan = "anda merupakan member"
    else:
        diskon_member = 0
        keterangan = "anda bukan member"

    total_diskon = diskon + diskon_member
    total_bayar_akhir = total_harga - total_diskon

# 5. Output Struk Transaksi
    print("=====================================")
    print("        STRUK TRANSAKSI SPBU         ")
    print("=====================================")
    print("Nama         :", nama_masuk           )
    print("NIM          :", nim_masuk            )
    print("Status       :", keterangan           )
    print("=====================================")
    print("Jenis BBM    :", jenis                )
    print("Harga/Liter  : Rp", harga             )
    print("Jumlah Liter :", liter                )
    print("=====================================")
    print("Total Harga  : Rp", total_harga       )
    print("Diskon Liter : Rp", diskon            )
    print("Diskon Member: Rp", diskon_member     )
    print("Total Diskon : Rp", total_diskon      )
    print("=====================================")
    print("TOTAL BAYAR  : Rp", total_bayar_akhir )
    print("=====================================")

else:
    print("Login gagal! Nama atau NIM tidak sesuai.")