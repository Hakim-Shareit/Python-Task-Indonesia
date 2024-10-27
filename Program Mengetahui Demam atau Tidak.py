S =input('Masukkan suhu tubuh Anda Dalam Bentuk Celcius : ')
try :
    H = int(S)
    print ('Berikut Hasil Diagnosanya : \n')
    print ('Suhu Tubuh Anda adalah ',S,' Derajat Celcius')
    if H <= 35 and H >= 33 :
        print ('Hipotermia Sedang')
    elif H <= 32 :
        print ('Hipotermia Berat')
    elif H >= 38 and H <= 39 :
        print ('Demam')
    elif H >= 40 :
        print ('Demam Tinggi')
    else:
        print ('Suhu Tubuh Anda Normal')
except :
    print ('Mohon Masukkan Nilai Suhu Tubuh Anda Dalam Bentuk Angka\n')