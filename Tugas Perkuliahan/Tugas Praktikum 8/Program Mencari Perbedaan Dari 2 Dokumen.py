def Beda():
    dok1 = input("Masukkan nama dokumen pertama: ")
    dok2 = input("Masukkan nama dokumen kedua: ")

    try:
        with open(dok1, 'r') as f1, open(dok2, 'r') as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()

        print("\nHasil Perbandingan Dokumen:")
        print("-" * 40)

        max_lines = max(len(content1), len(content2))
        for i in range(max_lines):
            line1 = content1[i].strip() if i < len(content1) else "<Baris tidak ada di file 1>"
            line2 = content2[i].strip() if i < len(content2) else "<Baris tidak ada di file 2>"

            if line1 != line2:
                print(f"Baris {i + 1}:")
                print(f"  File 1: {line1}")
                print(f"  File 2: {line2}")

        print("-" * 40)
        print("Perbandingan selesai.")
    except FileNotFoundError:
        print("Error: Salah satu file tidak ditemukan. Pastikan file berada di folder yang sama.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


Beda()