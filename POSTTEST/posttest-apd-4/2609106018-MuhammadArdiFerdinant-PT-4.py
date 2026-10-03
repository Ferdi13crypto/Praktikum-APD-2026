username_benar = "ferdi"
password_benar = "018"
saldo = 5000000
pin = "018018"
login = False
i = 1

for i in range(1,4):
    print("\n == SELAMAT DATANG DI BANK DIGITAL ==")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")
    if username_benar == username and password_benar == password:
        print("\nLogin Berhasil")
        login = True
        break
    elif username_benar != username and password_benar != password:
        print("\nUsername dan Password Salah")
    elif username_benar != username and password_benar == password:
        print("\nUsername Salah")
    elif username_benar == username and password_benar != password:
        print("\nPassword Salah")
    elif i == 3:
        print("\nKesempatan Anda Habis, Akun Anda Terblokir")

if login == True:
    pilihan = ""
    while pilihan != "2":
        print("\n=== MENU BANK DIGITAL ===")
        print(" 1. Transfer Uang")
        print(" 2. Logout")
        pilihan = input("Pilih Menu : ")
        if pilihan == "1":
            print("\n=== Menu Transfer ===")
            print(f"Saldo Saat Ini : {saldo}")
            username_penerima = input("Username Penerima : ")
            nominal_transfer = int(input("Masukkan Nominal Transfer : "))
            while nominal_transfer < 50000 or nominal_transfer > 1000000:
                if nominal_transfer < 50000:
                    print("Minimal Transfer 50000")
                    nominal_transfer = int(input("Masukkan Nominal Transfer Kembali: "))
                    status_transfer = True
                elif nominal_transfer > 1000000:
                    print("Maksimal Transfer 1000000")
                    nominal_transfer = int(input("Masukkan Nominal Transfer Kembali: ")) 
                    status_transfer = True
                elif saldo < nominal_transfer:
                    print("Saldo Anda Tidak Mencukupi")
                    nominal_transfer = int(input("Masukkan Nominal Transfer Kembali: "))
            print("\n=== KONFIRMASI TRANSAKSI ===")
            for i in range(1, 4):
                pin_input = input("Masukkan PIN Anda : ")
                if pin_input == pin:
                    print("Pin Benar")
                    break
                elif pin_input != pin:
                    print("Pin Salah, Silahkan Masukkan Pin Kembali")
            saldo = saldo - nominal_transfer
            print("\n=== Struk Bukti Transfer ===")
            print(f"Username Pengirim : {username}")
            print(f"Username Penerima : {username_penerima}")
            print(f"Nominal Transfer : {nominal_transfer}")
            lagi = input("Apakah Anda Ingin Melakukan Transfer Lagi? (y/n) : ")
            if lagi == "y":
                login = True
            elif lagi == "n":
                print("\nTerimakasih Telah Menggunakan Layanan Bank Digital")
                break 
        elif pilihan == "2":
            print("\nAnda Berhasil Logout, Terimakasih Telah Menggunakan Layanan Bank Digital")