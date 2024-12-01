def anagram(kata1, kata2):
    return sorted(kata1.lower()) == sorted(kata2.lower())

kata1 = input("Masukkan sebuah kata pertama: ")
kata2 = input("Masukkan sebuah kata kedua: ")

if anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukanlah anagram.")