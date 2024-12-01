def pemilah(kalimat):
    kata = kalimat.split()
    panjang = min(kata, key=len)
    pendek = max(kata, key=len)
    return pendek, panjang

kalimat = input("Masukkan sebuah kalimat: ")

pendek, panjang = pemilah(kalimat)
print(f"Kata terpendek: {pendek}, Kata terpanjang: {panjang}")