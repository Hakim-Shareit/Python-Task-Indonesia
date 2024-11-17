print ("Selamat datang di Kalkulator Deret Pintar\n")
N = int(input("Silahkan masukkan banyaknya bilangan : "))
total = 0
i = 1
deretan_nilai = ""

while i <= N:
    total += i
    if i == 1:
        deretan_nilai += f"{i}"
    else:
        deretan_nilai += f" + {i}"
    i += 1

rata_rata = total / N
print(f"Deretan nilai : {deretan_nilai}")
print(f"Total : {total}, Rata-rata : {rata_rata}")