angka1 = eval(input('Masukkan Angka Pertama = '))
angka2 = eval(input('Masukkan Angka Kedua = '))
angka3 = eval(input('Masukkan Angka Ketiga = '))

def cek_trio_ajaib(a, b, c):
 return (a + b == c) or (a + c == b) or (b + c == a) 

print ('Berikut Adalah hasilnya : ')

if cek_trio_ajaib(angka1, angka2, angka3):
    print ('True')
    print(angka1,',',angka2,',',angka3,',',' angka tersebut adalah trio ajaib')
else :
    print ('False')
    print(angka1,',',angka2 ,',',angka3,',','angka tersebut bukanlah trio ajaib')

