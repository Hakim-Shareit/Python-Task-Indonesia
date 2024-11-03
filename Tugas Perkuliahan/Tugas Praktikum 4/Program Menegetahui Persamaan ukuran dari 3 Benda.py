B1 = input('Masukkan Ukuran Benda Pertama : ')
B2 = input('Masukkan Ukuran Benda Kedua : ')
B3 = input('Masukkan Ukuran Benda Ketiga : ')

try :
    H1 = int(B1)
    H2 = int(B2)
    H3 = int(B3)
    if H1 == H2 and H2 == H3 :
        print ('ketiga benda ukurannya sama')
    elif H1 > H2 and H2 == H3 :
        print ('Kedua Benda ukurannya Sama')
    elif H2 > H1 and H1 == H3 :
        print ('Kedua Benda ukurannya Sama')
    elif H3 > H1 and H1 == H2 :
        print ('Kedua Benda ukurannya Sama')
    elif H1 < H2 and H2 == H3 :
        print ('Kedua Benda ukurannya Sama')
    elif H2 < H1 and H1 == H3 :
        print ('Kedua Benda ukurannya Sama')
    elif H3 < H1 and H1 == H2 :
        print ('Kedua Benda ukurannya Sama')
    else :
        print ('Tidak Ada ukuran yang Sama')
except :
    print ('Mohon Masukkan Dalam Bentuk Angka')