def konversi():
    f_to_c = lambda f: (f - 32) * 5/9
    c_to_f = lambda c: (c * 9/5) + 32

    print("Konversi Suhu Otomatis")
    print("1. Fahrenheit ke Celsius")
    print("2. Celsius ke Fahrenheit")

    Pilih = input("Pilih konversi (1/2): ")

    if Pilih == '1':
        Fah = float(input("Masukkan suhu dalam Fahrenheit: "))
        Cel = f_to_c(Fah)
        print(f"{Fah}°F = {f_to_c(Fah)}°C")
    elif Pilih == '2':
        Cel = float(input("Masukkan suhu dalam Celsius: "))
        Fah = c_to_f(Cel)
        print(f"{Cel}°C = {c_to_f(Cel)}°F")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

konversi()