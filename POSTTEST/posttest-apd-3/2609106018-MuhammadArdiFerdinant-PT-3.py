nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    print("Silahkan lanjut memilih tiket (Reguler, Premium, VIP)")
    jenis_tiket = input("Jenis tiket: ")
    if jenis_tiket == "Reguler":
        harga_tiket = 50000
        status_member = input("Status member: (Ya/Tidak) ")
        diskon = harga_tiket * 0.2 if status_member == "Ya" else 0
        biaya_admin = 0 if status_member == "Ya" else 2000
        total_bayar = harga_tiket - diskon + biaya_admin
        uang_bayar = int(input("Masukkan uang yang dibayar: "))

        if uang_bayar < total_bayar:
          print("Uang yang dibayarkan kurang. Struk tidak dapat dicetak")
        else:
          kembalian = uang_bayar - total_bayar
          print ("Struk Pembayaran")
          print ("Nama: ", nama)
          print ("Umur: ", umur)
          print ("Jenis Tiket: ", jenis_tiket)
          print ("Status Member: ", status_member)
          print ("total Bayar: ", total_bayar)
          print ("Kembalian: ", kembalian)

    elif jenis_tiket == "Premium":
        harga_tiket = 75000
        status_member = input("Status member: (Ya/Tidak) ")
        diskon = harga_tiket * 0.2 if status_member == "Ya" else 0
        biaya_admin = 0 if status_member == "Ya" else 2000
        total_bayar = harga_tiket - diskon + biaya_admin
        uang_bayar = int(input("Masukkan uang yang dibayar: "))

        if uang_bayar < total_bayar:
             print("Uang yang dibayarkan kurang. Struk tidak dapat dicetak")
        else:
          kembalian = uang_bayar - total_bayar
          print ("Struk Pembayaran")
          print ("Nama: ", nama)
          print ("Umur: ", umur)
          print ("Jenis Tiket: ", jenis_tiket)
          print ("Status Member: ", status_member)
          print ("total Bayar: ", total_bayar)
          print ("Kembalian: ", kembalian)

    elif jenis_tiket == "VIP":
        harga_tiket = 100000
        status_member = input("Status member: (Ya/Tidak) ")
        diskon = harga_tiket * 0.2 if status_member == "Ya" else 0
        biaya_admin = 0 if status_member == "Ya" else 2000
        total_bayar = harga_tiket - diskon + biaya_admin
        uang_bayar = int(input("Masukkan uang yang dibayar: "))

        if uang_bayar < total_bayar:
             print("Uang yang dibayarkan kurang. Struk tidak dapat dicetak")
        else:
          kembalian = uang_bayar - total_bayar
          print ("Struk Pembayaran")
          print ("Nama: ", nama)
          print ("Umur: ", umur)
          print ("Jenis Tiket: ", jenis_tiket)
          print ("Status Member: ", status_member)
          print ("total Bayar: ", total_bayar)
          print ("Kembalian: ", kembalian)

    else:
        print("Jenis tiket tidak valid")
