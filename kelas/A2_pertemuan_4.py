# batas = 5
# for i in range(70):
#     print("Perulangan ke-", i)

# nilai = [10, 20, 30, 40, 50]
# for hitam in nilai:
#     if hitam > 10:
#         print("lulus")
#     else: print("tidak lulus")

# for i in range(0, 11, 2): # start, stop, step
#     print(i)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# while True:
#     print("hello")

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")

# print(f"Total Perulangan : {hitung}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# bilangan = int(input("masukkan bilangan: "))

# for i in range(bilangan+1):
#     if i % 2 == 0:
#         continue
#     print("jumlah bilangan ganjil yang di temukan: ", i)

uang = int(input("masukkan jumlah uang uang saku awal: "))

while(uang > 0):
    nominal = int(input("masukkan nominal setiap pengeluaran: "))
    uang -= nominal
    print(f"Saldo sekarang: {uang}")
    break

print(f"Total saldo akhir : {nominal}")