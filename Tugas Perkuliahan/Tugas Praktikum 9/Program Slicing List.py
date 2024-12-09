# List (A-Z)
import string
alfabet = list(string.ascii_uppercase)

# 5 huruf pertama
lima_pertama = alfabet[:5]

# Huruf ke-3 sampai ke-7
huruf_3_7 = alfabet[3:8]

# Balik urutan huruf
balik_urutan = alfabet[::-1]

# List yang berisi setiap huruf ke-2
huruf_ke_2 = alfabet[::2]

# Menampilkan Hasil
print("5 huruf pertama:", lima_pertama)
print("Huruf 3 sampai 7:", huruf_3_7)
print("Balik urutan:", balik_urutan)
print("Huruf ke-2:", huruf_ke_2)