B =input('Masukkan Bulan Keberapa : ')

try :
    H = int(B)
    print ('Berikut hasilnya :\n')
    
    if H == 1 :
        print ('Bulan Januari berjumlah 31 hari')
    elif H == 2 :
        print ('Bulan Februari berjumlah 28 atau 29 hari')
    elif H == 3 :
        print ('Bulan Januari berjumlah 31 hari')
    elif H == 4 :
        print ('Bulan Januari berjumlah 30 hari')
    elif H == 5 :
        print ('Bulan Januari berjumlah 31 hari')
    elif H == 6 :
        print ('Bulan Januari berjumlah 30 hari')
    elif H == 7 :
        print ('Bulan Januari berjumlah 31 hari')
    elif H == 8 :
        print ('Bulan Januari berjumlah 31 hari')
    elif H == 9 :
        print ('Bulan Januari berjumlah 30 hari')
    elif H == 10 :
        print ('Bulan Januari berjumlah 31 hari')
    elif H == 11 :
        print ('Bulan Januari berjumlah 30 hari')
    elif H == 12 :
        print ('Bulan Januari berjumlah 31 hari')
    else:
        print ('Hanya terdapat 12 bulan')
except :
    print ('Mohon Masukkan Jawaban Dalam Bentuk Angka')