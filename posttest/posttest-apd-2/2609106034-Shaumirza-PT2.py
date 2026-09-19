# 1. Diketahui sebuah maskapai penerbangan sedang mengalkulasi berat bagasi kabin (dalam satuan Kilogram) untuk 6 penumpang di baris pertama. Data berat tersebut disimpan dalam variabel berikut:
bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

# Poin Plus (+): Menggunakan list (bagasi_1 dst diisi ke dalam list
bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

# 2. Pihak maskapai menerapkan biaya kompensasi bahan bakar tambahan sebesar 5% dari total akumulasi berat seluruh bagasi kelompok tersebut. Bantulah petugas check-in untuk menghitung berat total akhir sebagai dasar kalkulasi biaya! (Menghitung total berat tidak boleh menggunakan SUM, harus dijumlahkan manual dan disimpan di variabel total_berat_akhir).
total_berat_akhir = bagasi[0] + bagasi[1] + bagasi[2] + bagasi[3] + bagasi[4] + bagasi[5]
kompensasi = total_berat_akhir * 0.05

# 3. Hitung rata-rata berat bagasi per orang dengan membuat variabel bernama rata_rata yang berisi variabel total_bayar dibagi dengan banyak data (diperbolehkan menggunakan fungsi len()).
rata_rata = total_berat_akhir / len(bagasi)

# 4. Buat va riabel bernama nim yang diisi dengan 2 digit terakhir NIM.
nim = 34

# 5. Buat variabel bernama bolean yang isinya nim < rata_rata.
boolean = nim < rata_rata

# Poin Plus (+): )Gunakan metode list slicing untuk mengambil dan menampilkan data penumpang yang berada di posisi tengah saja (yaitu indeks ke-2 hingga indeks ke-4)
penumpan_tengah = bagasi[2:5]

# Poin Plus (+): Konversikan total berat akhir ke satuan gram
konversi_gram = total_berat_akhir * 1000

# 6. Tampilkan semua nilai variabel yang ada menggunakan perintah print().
print("bagasi 1:", bagasi_1)
print("bagasi 2:", bagasi_2)
print("bagasi 3:", bagasi_3)
print("bagasi 4:", bagasi_4)
print("bagasi 5:", bagasi_5)
print("bagasi 6:", bagasi_6)
print("data bagasi penumpang:", bagasi)
print("kompensasi:", kompensasi)
print("rata rata berat bagasi per orang:", rata_rata)
print("nim:", nim)
print("boolean:", boolean)

# Poin Plus (+)
print("data penumpang posisi tengah:", penumpan_tengah)
print("total berat akhir kilogram:", total_berat_akhir)
print("total berat akhir gram:", konversi_gram)