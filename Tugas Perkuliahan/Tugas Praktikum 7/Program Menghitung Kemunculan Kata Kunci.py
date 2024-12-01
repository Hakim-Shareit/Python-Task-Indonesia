def hitung(teks, kata_kunci):
    return teks.lower().count(kata_kunci.lower())


teks = input("Masukkan teks berita: ")
kata_kunci = input("Masukkan kata kunci: ")

jumlah = hitung(teks, kata_kunci)
print(f"Kata '{kata_kunci}' muncul sebanyak {jumlah} kali dalam teks.")