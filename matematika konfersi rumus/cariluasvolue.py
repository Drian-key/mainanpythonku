print("=====Menghitung luas dan volume bangun ruang=====")

def mulaiGame():
	menu = input("Cari apa?'\n 1.Kubus \n 2.Balok \n 3.Prisma \n 4.Limas \n 5.Kerucut \n 6.Tabung \n 7.Bola \n Input menu:")
	if menu == "1":
		Kubus()
	elif menu == "2":
		Balok()
	elif menu == "3":
		borong()
	elif menu == "4":
		keluar()
	else:
		print("Maaf tidak ada di menu :v")
		mulaiGame()
    
def Kubus():
    print("\n\n\n\n\n=====Menghitung Kubus=====")
    sisi = int(input("Masukan sisinya:"))
    luas = 6 * sisi**2
    volume = sisi**3
    print("Luasnya adalah: " + str(luas) + "\nVolumenya adalah: " + str(volume))

def Balok():
    print("\n\n\n\n\n=====Menghitung Balok=====")
    plt = [int(input("panjang: ")), int(input("lebar: ")), int(input("tinggi: "))]
    luas = 2 * (plt[0] + plt[1] + plt[2])
    volume = plt[0] * plt[1] * plt[2]
    print("Luasnya adalah: " + str(luas) + "\nVolumenya adalah: " + str(volume))


mulaiGame()