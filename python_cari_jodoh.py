"""
mencari jodoh baik & rajin
"""

nama = input("Nama kamu:")
miskin = input("Kaya atau ngak?:")
ganteng = input("Ganteng apa ngak:")

if (miskin == "kaya") & (ganteng == "ganteng"):
	print(nama,"kamu idaman")
elif (miskin == "ngak") & (ganteng == "ganteng"):
	print(nama, "kalo ganteng gpp")
elif (miskin == "kaya") & (ganteng == "ngak"):
	print(nama, "gpp kok ngak ganteng yang penting kan kaya")
elif (miskin == "ngak") & (ganteng == "ngak"):
	print(nama, "tolol, gila lu yak udah jelek miskin, Ogah banget gw. najiss.")
else:
	print("Lu orang stress")


# if 1 == 0:
# 	print("Selamat buat temenmu")
# else:
# 	print("Tebakan salah")