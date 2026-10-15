import os

bersih = "cls" if os.name == "nt" else "clear"

Role = ("atmin", "yahaha user")
value = ("merek","ukuran", "harga")

data_user = [
    ["atminperdi", "atmin123", Role[0]],
    ["budi", "budikuy", Role[1]],
]

data_sepatu = [
    ["adidas", 40, 2000000],   
    ["ortus", 42, 3000000],
    ["asics", 41, 1500000],
] 
#program utama
jalan = True
while jalan:
    os.system(bersih)
    print("SISTEM PENCATAT STOK SEPATU RUNNING")
    print("=" * 50)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu (1-3): ")
#cara login
    if menu_awal == "1":
        percobaan = 0
        user_aktif = None
        while percobaan < 3 and user_aktif is None:
            os.system(bersih)
            print("---LOGIN---")
            username = input("Username: ")
            password = input("Password: ")
            for i in data_user:
                if i[0] == username and i[1] == password:
                    user_aktif = i
            if user_aktif is None:
                percobaan += 1
                print(f"Username atau password salah wok Sisa percobaanmu: {3 - percobaan}")
                input("Tekan enter kalo mau lanjut wok")
 
        if user_aktif is None:
            print("Terlalu banyak percobaan lu. sana kembali ke menu awal.")
            input("pencet enter kalo mau lanjut wok")
        else:
            nama = user_aktif[0]
            role = user_aktif[2]
            sesi = True
#after login
            while sesi:
                os.system(bersih)
                print(f"ciee bisa login: {nama} ({role})")
                print("=" * 50)
                if role == Role[0]:
                    print("1. Lihat Data Sepatu    (Read)")
                    print("2. Tambah Sepatu        (Create)")
                    print("3. Ubah Data Sepatu     (Update)")
                    print("4. Hapus Data Sepatu    (Delete)")
                    print("0. Logout")
                else:
                    print("1. Lihat Data Sepatu")
                    print("0. Logout")
                pilih = input("Pilih menu dulu: ")
#READ
                if pilih == "1":
                    os.system(bersih)
                    print("--- DAFTAR SEPATU RUNNING ---")
                    if len(data_sepatu) == 0:
                        print("Belum ada data sepatu weh")
                    else:
                        (k1, k2, k3) = value
                        print(f"{'No':<4}{k1:<16}{k2:<10}{k3:>14}")
                        print("-" * 50)
                        for i in range(len(data_sepatu)):
                            (merek, ukuran, harga) = data_sepatu[i]
                            print(f"{i + 1:<4}{merek:<16}{ukuran:<10}{harga:>14,}")
                    input("\nPencet enter kalo mau kembali yak")
#CREATE
                elif pilih == "2" and role == Role[0]:
                    os.system(bersih)
                    print("--- TAMBAH DATA SEPATU ---")
                    while True:
                        merek = input("Merek          : ")
                        if merek != "":
                            break
                        print("Merek jangan kosong cuy")
                    while True:
                        ukuran = input("Ukuran (30-50) : ")
                        if ukuran.isdigit() and 30 <= int(ukuran) <= 50:
                            ukuran = int(ukuran)
                            break
                        print("Ukurannya harus antara 30 sampai 50 yak")
                    while True:
                        harga = input("Harga (Rp)     : ")
                        if harga.isdigit() and int(harga) > 0:
                            harga = int(harga)
                            break
                        print("Harga harus lebih dari 0, kalo engga ya gratis dong..")
 
                    duplikat = False
                    for s in data_sepatu:
                        if s[0] == merek and s[1] == ukuran and s[2] == harga:
                            duplikat = True
                    if duplikat:
                        print("Gagal! Data sepatu sudah ada bos.")
                    else:
                        data_sepatu.append([merek, ukuran, harga])
                        print("Gokill data sepatu berhasil nambah tuh")
                    input("Pencet enter kalo mau kembali yak")
#UPDATE
                elif pilih == "3" and role == Role[0]:
                    os.system(bersih)
                    print("--- UBAH DATA SEPATU ---")
                    if len(data_sepatu) == 0:
                        print("gaada sepatu yang mau diubah wok")
                    else:
                        (k1, k2, k3) = value
                        print(f"{'No':<4}{k1:<16}{k2:<10}{k3:>14}")
                        print("-" * 44)
                        for i in range(len(data_sepatu)):
                            (merek, ukuran, harga) = data_sepatu[i]
                            print(f"{i + 1:<4}{merek:<16}{ukuran:<10}{harga:>14,}")
 
                        nomor = input("\nNomor sepatu yang diubah: ")
                        if nomor.isdigit() and 1 <= int(nomor) <= len(data_sepatu):
                            idx = int(nomor) - 1
                            print("1. Ubah Merek")
                            print("2. Ubah Ukuran")
                            print("3. Ubah Harga")
                            print("4. Ubah Ukuran & Harganya sekalian lahh")
                            bagian = input("Apa yang mau diubah bos: ")
 
                            if bagian == "1":
                                while True:
                                    merek = input("Merek apa bos : ")
                                    if merek != "":
                                        break
                                    print("Merek jangan kosong woii")
                                data_sepatu[idx][0] = merek             
                                print("Gokill merek diubah nichh")
                            elif bagian == "2":
                                while True:
                                    ukuran = input("Mau ukuran berape lu (30-50): ")
                                    if ukuran.isdigit() and 30 <= int(ukuran) <= 50:
                                        ukuran = int(ukuran)
                                        break
                                    print("Ukuran harus 30-50 yak")
                                data_sepatu[idx][1] = ukuran            
                                print("Gokill ukuran diubah nichh")
                            elif bagian == "3":
                                while True:
                                    harga = input("Harganya mau berapa bos (Rp): ")
                                    if harga.isdigit() and int(harga) > 0:
                                        harga = int(harga)
                                        break
                                    print("Harga ")
                                data_sepatu[idx][2] = harga             
                                print("gokss harganya diubah tuh")
                            elif bagian == "4":
                                while True:
                                    ukuran = input("Mau ukuran berape lu (30-50): ")
                                    if ukuran.isdigit() and 30 <= int(ukuran) <= 50:
                                        ukuran = int(ukuran)
                                        break
                                    print("Ukuran harus 30-50 yak")
                                while True:
                                    harga = input("Harganya mau berapa bos (Rp) ")
                                    if harga.isdigit() and int(harga) > 0:
                                        harga = int(harga)
                                        break
                                    print("Harga harus lebih dari 0, kalo engga ya gratis dong..")
                                data_sepatu[idx][1:3] = [ukuran, harga] 
                                print("gokss ukuran sama harganya udah diubah nih")
                            else:
                                print("ngawur, masukkin yang bener kocak")
                        else:
                            print("nomornya ga valid wok")
                    input("Pencet enter kalo mau kembali yak")
#DELETE
                elif pilih == "4" and role == Role[0]:
                    os.system(bersih)
                    print("--- HAPUS DATA SEPATU ---")
                    if len(data_sepatu) == 0:
                        print("Belum ada datanya, apa yang mau dihapus kocak")
                    else:
                        (k1, k2, k3) = value
                        print(f"{'No':<4}{k1:<16}{k2:<10}{k3:>14}")
                        print("-" * 50)
                        for i in range(len(data_sepatu)):
                            (merek, ukuran, harga) = data_sepatu[i]
                            print(f"{i + 1:<4}{merek:<16}{ukuran:<10}{harga:>14,}")
 
                        nomor = input("\nMau sepatu apa yang dihapus cuy: ")
                        if nomor.isdigit() and 1 <= int(nomor) <= len(data_sepatu):
                            idx = int(nomor) - 1
                            yakin = input(
                                f"Yakin mau dihapus {data_sepatu[idx][0]} ukuran {data_sepatu[idx][1]}? (y/n): "
                            )
                            if yakin == "y":
                                dihapus = data_sepatu.pop(idx)
                                print(f"{dihapus[0]} ukuran {dihapus[1]} berhasil dihapus wok")
                            elif yakin == "n":
                                print("Penghapusan batal yak")
                            else:
                                print("Isi yang bener wehh, pernghapusan batal yak.")
                        else:
                            print("isi yang bener kocak")
                    input("Pencet enter kalo mau kembali yak")
#LOGOUT
                elif pilih == "0":
                    sesi = False
 
                else:
                    print("Isi yang bener kocak")
                    input("pencet enter kalo mau lanjut wok")
#REGISTER
    elif menu_awal == "2":
        os.system(bersih)
        print("--- REGISTER AKUN BARU ---")
        username = input("Username (minimal 3 karakter, jangan spasi): ")
        password = input("Password (minimal 6 karakter): ")
 
        terpenuhi = False
        for u in data_user:
            if u[0] == username:
                terpenuhi= True
 
        if len(username) < 3 or " " in username:
            print("Username minimal 3 karakter dan jangan spasi")
        elif terpenuhi:
            print("Username dah dipake wok, makanya nama jangan pasaran")
        elif len(password) < 6:
            print("Password minimal 6 karakter yak")
        else:
            data_user.append([username, password, Role[1]])
            print("Gokss akun baru, login dah")
        input("pencet enter kalo mau lanjut wok")
#KELUAR
    elif menu_awal == "3":
        print("Makasih yak, selesai deh")
        jalan = False
 
    else:
        print("Isi yang bener wok")
        input("pencet enter kalo mau lanjut wok")
