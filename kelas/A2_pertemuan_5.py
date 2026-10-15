# nama1 = "ezra"
# nama2 = "zaidan"
# nama3 = "messi"

# print(nama1,nama2,nama3)

# print("======================")
# list_nama = ["ezra","zaidan","messi"]
# print(list_nama)

# print("======================")
# for i in(list_nama[:2]):
#     print(i)

# print("======================")
# list_nama.append("ammar")
# print(list_nama)

# print("======================")
# list_nama.extend(["mirza","wili"])
# print(list_nama)

# print("======================")
# list_nama.insert(2, "konrad")
# print(list_nama)

# print("======================")
# list_nama[:3] = ["hafiz","truffert","kafar"]
# print(list_nama)

# print("======================")
# del list_nama[1]
# print(list_nama)

# print("======================")
# list_nama.remove("wili")
# print(list_nama)

# print("======================")
# ambil_nama = list_nama.pop(1)
# print(list_nama)
# print(ambil_nama)

# print("======================")
# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# print("======================")
# for i in line_up:
#     for j in i:
#         print(j)

# print("======================")
# nama = ["ezra","zaidan","uma"]
# print(nama)
# hapus = int(input("masukkan nama yang ingin di hapus: "))
# del nama[hapus]
# print(nama)

# print("======================")
# point=[1,2,3,4,5,6,7]
# print(point[1:5:2])

# print("======================")
# point1 = [1,2,3,4,5,6,7]
# point2 = [8,9,10]
# poin = point1 + point2
# print(poin)

# print("======================")
# point=[1,2,3,4,5,6,7]
# print(point)

# print("======================")
# point[4:7] = [11,12,13]
# print(point)

print("======================")
nama = ("fachry", "zaidan", "ammar", "ezra")
print(nama)

listnama = list(nama)
listnama.append("margarito")
nama = tuple(listnama)

print(nama)

print("======================")
game = ("ml","genshin")
(moba, open_world) = game

print(moba)
print(open_world)