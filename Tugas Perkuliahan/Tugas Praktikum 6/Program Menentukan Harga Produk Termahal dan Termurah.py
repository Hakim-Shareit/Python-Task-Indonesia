print("Program Harga Tertinggi dan Terendah:")
print("Ketik 'stop' bila ingin berhenti\n")

harga_produk = []
hitung = 0

while True:
    harga = input(f"Harga produk ke-{hitung + 1}: ")
    if harga.lower() == "stop":
        break
    try:
        harga_produk.append(float(harga))
        hitung += 1
    except:
        print("Input tidak valid. Masukkan angka atau 'stop'.")

if harga_produk:
    print(f"Harga Tertinggi: {max(harga_produk)}")
    print(f"Harga Terendah: {min(harga_produk)}")
else:
    print("Tidak ada harga yang dimasukkan.")
