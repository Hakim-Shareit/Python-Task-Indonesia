bil1 = eval(input('Masukkan Kode Produk Pertama = '))
bil2 = eval(input('Masukkan Kode Produk Kedua = '))
bil3 = eval(input('Masukkan Kode Produk Ketiga = '))

print ('Dari Beberapa Kode Produk Berikut :')
print (bil1,',',bil2,',dan',bil3,)

def satuan_produk(kode1, kode2, kode3):
    satuan1 = kode1 % 10
    satuan2 = kode2 % 10
    satuan3 = kode3 % 10
    return (satuan1 == satuan2) or (satuan1 == satuan3) or (satuan2 == satuan3)

print('Hasilnya Kecocokan Produk Adalah = ',satuan_produk(bil1,bil2,bil3))