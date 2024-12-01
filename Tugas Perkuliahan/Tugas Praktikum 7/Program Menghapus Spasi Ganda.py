def hapus_spasi(teks):
    while "  " in teks:
        teks = teks.replace("  ", " ")
    return teks

teks = input("Masukkan teks berspasi ganda : ")

hasil = hapus_spasi(teks)
print("Hasil setelah diperbaiki :", hasil)