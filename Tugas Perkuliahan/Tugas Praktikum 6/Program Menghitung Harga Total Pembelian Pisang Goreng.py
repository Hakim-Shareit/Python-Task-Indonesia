jumlah = int(input("Masukkan jumlah pisang goreng yang ingin dihitung: \n"))
harga = int(input("Masukkan harga 1 buah pisang goreng: \n"))
print ("Rincianm Pembelian")
total_harga = 0
p = 1
print (f"Satu buah pisang goreng seharga Rp.{harga}, dengan total pembelian sebanyak : {jumlah} buah\n")

while p <= jumlah:
    total_harga += harga
    p += 1

print(f"Maka total harga adalah : Rp.{total_harga}")