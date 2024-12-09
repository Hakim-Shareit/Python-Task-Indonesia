# Input
list_strings = input("Masukkan angka (pisahkan dengan koma): ").split(',')

# list bilangan bulat
angka = [int(x) for x in list_strings]

# list genap
genap = [x for x in angka if x % 2 == 0]

# Menampilkan hasil
print("Angka genap:", genap)
