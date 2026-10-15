# kartu = ["merah", "merah", "biru", "hijau"]
# print(len(kartu))

# print("======================")
# set_baru = set(kartu)
# print(kartu)

# print("======================")
# kartu2 = {"merah", "merah", "biru", "hijau"}
# kartu2.discard("kuning")
# kartu2.remove("merah")

# for i in kartu2:
#     print(i)

# print("======================")
# aslab1 = {"ezra", "rasyiq", "zaidan"}
# aslab2 = {"rasya", "attalah", "farren"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# print("======================")
# Biodata = {
#         "Nama" : "Siti Julpa",
#         "NIM" : 25091060,
#         "KRS" : ["Struktur Data", "Basis Data"],
#         "Mahasiswa_Aktif" : True,
#         "Instagram" : "julpatarr"
# }

# print(Biodata["Instagram"])
# print(Biodata["Mahasiswa_Aktif"])

# print("======================")
# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)

# for keys, value in game.items():
#     print(f"{keys} adalah jenis game {value}")

# game.update({"resident evil" : "horror"})
# print(game)

# tambah = game.setdefault("resident evil", "horror")
# print(game)

# print("======================")
# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000, 14000
# menu = dict.fromkeys(key, value)
# print(menu)

# print("======================")
# menu = {
# "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
# "nasi" : ["nasi goreng", "nasi uduk"],
# "mie" : ["mie goreng rendang", "mie goreng aceh"],
# "kuah" : ["soto", "rawon", "sop iga"]
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#         print(kategori)
#     print("")

# print("======================")
# data = {
#     "siswa1" :{
#         "nama" : "ezra",
#         "kelas" : "A2",
#         "Nilai" : 85
#     },
#     "siswa2" :{
#         "nama" : "zaidan",
#         "kelas" : "A2",
#         "Nilai" : 95
#     }
# }

# print(data["siswa1"]["nama"])
# print(data["siswa2"]["nama"])

print("======================")
poli_umum = {"Andi", "Budi", "Citra", "Doni"}
poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
gabunf = poli_umum.union(poli_gigi)
print(gabunf)

print("======================")