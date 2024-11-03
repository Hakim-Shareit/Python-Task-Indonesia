B =input('Masukkan Nilai : ')
try :
    H = int(B)
    print ('Berikut adalah hasilnya :')
    print ('Angka yang anda masukan adalah : \n',B)
    print ('Bilangan tersebut termasuk : ')
    if H == 0 :
        print ('Nol')
    elif H < 0 :
        print ('Negatif')
    elif H > 0 :
        print ('Positif')
except :
    print ('Mohon Masukkan Dalam Bentuk Angka\n')