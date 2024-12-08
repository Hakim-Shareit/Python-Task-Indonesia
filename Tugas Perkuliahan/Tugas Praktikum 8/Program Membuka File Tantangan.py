def kuis():
    filenya = input("Masukkan nama file soal: ")

    try:
        with open(filenya, 'r') as file:
            coba = file.readlines()

        benar = 0
        total = 0

        for line in coba:
            if line.startswith("Jawaban:"):
                jawaban = line.split(":",1)[1].strip()
                total += 1
                jawabanmu = input("Masukkan jawaban Anda: ").strip()

                if jawabanmu.lower() == jawaban.lower():
                    print("Benar!\n")
                    benar += 1
                else:
                    print(f"Salah! Jawaban yang benar adalah: {jawaban}\n")
            elif line.strip():
                print(line.strip())

        print(f"Anda menjawab {benar} dari {total} soal dengan benar.")
    except FileNotFoundError:
        print("Error: File tidak ditemukan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    kuis()