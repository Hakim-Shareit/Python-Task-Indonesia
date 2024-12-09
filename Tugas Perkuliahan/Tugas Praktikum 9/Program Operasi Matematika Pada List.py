# Daftar list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 10, 15, 20, 25]

# Penjumlahkan kedua list
penjumlahan = [a + b for a, b in zip(list1, list2)]

# Perkalian Kedua list
perkalian = [x * 2 for x in list1]

# Nilai terbesar dan terkecil
nilai_terbesar = max(max(list1), max(list2))
nilai_terkecil = min(min(list1), min(list2))

# Hitung rata-rata dari kedua list
rata_rata = sum(list1 + list2) / len(list1 + list2)

print("Penjumlahan:", penjumlahan)
print("Perkalian:", perkalian)
print("Nilai terbesar:", nilai_terbesar)
print("Nilai terkecil:", nilai_terkecil)
print("Rata-rata:", rata_rata)
