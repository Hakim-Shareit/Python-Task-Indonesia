print ("Program Menghitung Indeks Prestasi Semester : \n")
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))
total_sks = 0
total_nilai = 0
i = 0

while i < jumlah_mata_kuliah:

    sks = int(input(f"Masukkan jumlah SKS untuk mata kuliah ke-{i + 1}: "))
    nilai = input(f"Masukkan nilai (A, B, C, D, atau E) untuk mata kuliah ke-{i + 1}: ").upper()
        
    if nilai == 'A':
        bobot = 4
    elif nilai == 'B':
        bobot = 3
    elif nilai == 'C':
        bobot = 2
    elif nilai == 'D':
        bobot = 1
    elif nilai == 'E':
        bobot = 0
    else:
        print("Nilai tidak valid. Masukkan A, B, C, D, atau E.")
        continue
    total_sks += sks
    total_nilai += bobot * sks
    i += 1 

ips = total_nilai / total_sks
print(f"\nIPS Anda: {ips:.2f}")