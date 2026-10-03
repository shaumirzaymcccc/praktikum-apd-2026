# angka = 11

# if angka < 10: # Kondisi percabangan IF
#     print("Angka kurang dari 10")

# umur = int(input("Masukkan umur: ")) # Input umur
# # Misalkan, umur = 17
# if umur >= 17:
#     print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena kondisi True
# else:
#     print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan

# kendaraan = input("Masukkan jenis kendaraan anda: ").lower()
# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000

# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# nilai = int(input("masukkan nilai: "))

# if nilai >= 10:
#     if nilai >= 20:
#         if nilai >= 30:
#             print("angka besar")
#         print("angka sedang")
#     print("angka kecil")

#STUDI KASUS 1

umur = int(input("masukkan umur: "))
status = "boleh masuk event" if umur >= 18 else "ga boleh masuk event"
print(status)

#STUDI KASUS 2

pembelian = int(input("masukkan harga beli: "))

if pembelian > 200000:
    print("diskon 30%")
elif pembelian > 100000:
    print("diskon 10%")
elif pembelian <= 100000:
    print("tidak mendapatkan diskon")
else:
    print("diskon tidak dapat di akumulasi kan")