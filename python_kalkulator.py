print("SELAMAT DATANG DI KALKULATOR PYTHON")
nama = input("Siapa kamu:")

def Menu():
    Pilih = input("Menu pilihan:\n1.Penjumlahan\n2.pengurangan\n3.Perkalian\n4.Pembagian\n5.Pangkat\n"+ nama +" input pilihan kamu disini:")
    if (Pilih == "1"):
        print("Penjumlahan")
        Jumlah()
    elif (Pilih == "2"):
        print("Pengurangan")
        Kurang()
    elif (Pilih == "3"):
        print("Perkalian")
        Kali()
    elif (Pilih == "4"):
        print("Pembagian")
        Bagi()
    elif (Pilih == "5"):
        print("Pangkat")
        Pangkat()
    else:
        print("tidak ada di menu")
        Menu()
    
def Jumlah():
    Ap = int(input("Masukan angka pertama:"))
    Ak = int(input("Masukan angka kedua:"))
    hasil = Ap + Ak
    print("hasilnya adalah:" + str(hasil))
    back = input("Masukan angka 0 untuk keluar dan 1 untuk menjumlah lagi:")
    if (back == "0"):
        Menu()
    elif (back == "1"):
        Jumlah()
    else:
        print("tidak ada di menu")
        Jumlah()

def Kurang():
    Ap = int(input("Masukan angka pertama:"))
    Ak = int(input("Masukan angka kedua:"))
    hasil = Ap - Ak
    print("hasilnya adalah:" + str(hasil))
    back = input("Masukan angka 0 untuk keluar dan 1 untuk lagi:")
    if (back == "0"):
        Menu()
    elif (back == "1"):
        Kurang()
    else:
        print("tidak ada di menu")
        Kurang()

def Kali():
    Ap = int(input("Masukan angka pertama:"))
    Ak = int(input("Masukan angka kedua:"))
    hasil = Ap * Ak
    print("hasilnya adalah:" + str(hasil))
    back = input("Masukan angka 0 untuk keluar dan 1 untuk lagi:")
    if (back == "0"):
        Menu()
    elif (back == "1"):
        Kali()
    else:
        print("tidak ada di menu")
        Kali()

def Bagi():
    Ap = int(input("Masukan angka pertama:"))
    Ak = int(input("Masukan angka kedua:"))
    hasil = Ap / Ak
    print("hasilnya adalah:" + str(hasil))
    back = input("Masukan angka 0 untuk keluar dan 1 untuk lagi:")
    if (back == "0"):
        Menu()
    elif (back == "1"):
        Bagi()
    else:
        print("tidak ada di menu")
        Bagi()

def Pangkat():
    Ap = int(input("Masukan angka pertama:"))
    Ak = int(input("Masukan angka kedua:"))
    hasil = Ap ** Ak
    print("hasilnya adalah:" + str(hasil))
    back = input("Masukan angka 0 untuk keluar dan 1 untuk lagi:")
    if (back == "0"):
        Menu()
    elif (back == "1"):
        Pangkat()
    else:
        print("tidak ada di menu")
        Pangkat()


Menu()
