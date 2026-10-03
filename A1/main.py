nama = "fadil"
nim = 36

while True:
    Nama = str(input("Masukkan Nama Anda : "))
    Nim = int(input("Masukkan NIM Anda : "))
    if Nama == nama and Nim == nim:
        print("Login Berhasil")
        False
        break
    elif Nama == nama and Nim != nim:
        print("NIM Salah")
    elif Nama != nama and Nim == nim:
        print("Nama Salah")
    else:
        print("Nama dan NIM Salah")

pulau = str(input("Masukkan Nama Pulau : "))
if pulau == "Kalimantan":
    lahan = str(input("Masukkan Nama Lahan : "))
    if lahan == "Gambut":
            titik_api = int(input("Masukkan Titik Api : "))
            luas_lahan = titik_api*5
            print(f"Luas lahan gambut adalah {luas_lahan} hektar")
            user = str(input("Apakah Anda ingin menghitung luas lahan lain? (ya/tidak) : "))
    elif lahan == "Mineral":
        titik_api = int(input("Masukkan Titik Api : "))
        luas_lahan = titik_api*5
        print(f"Luas lahan mineral adalah {luas_lahan} hektar")
    else:
        print("Lahan Tidak Ditemukan")
elif pulau == "Sumatera":
    lahan = str(input("Masukkan Nama Lahan : "))
    if lahan == "Gambut":
        titik_api = int(input("Masukkan Titik Api : "))
        luas_lahan = titik_api*5
        print(f"Luas lahan gambut adalah {luas_lahan} hektar")
    elif lahan == "Mineral":
        titik_api = int(input("Masukkan Titik Api : "))
        luas_lahan = titik_api*5
        print(f"Luas lahan mineral adalah {luas_lahan} hektar")
    else:
        print("Lahan Tidak Ditemukan")