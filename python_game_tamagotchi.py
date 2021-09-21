

#cara pertama

# nama = input("Nama monsternya siapa?:")
# monster = {"Nama": nama, "Power": 100}


# def mulaiGame():
# 	menu = input("Mau ngapain?'\n 1.Makan \n 2.Cek Status \n 3.Keluar")
# 	if menu == "1":
# 		print("Shaaa, aku bertambah kuattt")
# 		monster["Power"] += 100
# 		mulaiGame()
# 	elif menu == "2":
# 		print("Status monster" + nama)
# 		print(monster)
# 		mulaiGame()
# 	else:
# 		print("bye bye")


# mulaiGame()


#cara kedua
nama = input("Namamu siapa?:")
mu = {"nama": nama, "Berat": 35}


def mulaiGame():
	menu = input("Mau ngapain?'\n 1.Makan \n 2.Cek Status \n 3.Makan 10 kali \n 4.Keluar \n Input menu:")
	if menu == "1":
		makan()
	elif menu == "2":
		status()
	elif menu == "3":
		borong()
	elif menu == "4":
		keluar()
	else:
		print("Maaf tidak ada di menu :v")
		mulaiGame()

def makan():
		mu["Berat"] += 2
		print("Wkwkwk kamu gendut....")
		keluar = input("Tekan 0 untuk kemenu atau 1 untuk makan lagi: ")
		if keluar == "0":
			mulaiGame()
		elif keluar == "1":
			print("kamu tambah gendut")
			makan()

def status():
		print("Status mu!")
		print("Nama  :" + nama)
		print("Berat :" + str(mu["Berat"]) + "Kg")
		keluar = input("Tekan 0 untuk kemenu: ")
		if keluar == "0":
			mulaiGame()
		else:
			print("Silahkan input 0 untuk ke menu")
			status()

def borong():
		print("Kamu makan 10 kali, wkwkwk hebat")
		mu["Berat"] += 20
		keluar = input("Tekan 0 untuk kemenu: ")
		if keluar == "0":
			mulaiGame()

def keluar():
	print("bye bye " + nama)

mulaiGame()