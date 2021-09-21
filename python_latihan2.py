# import datetime

# now = datetime.datetime.now()


# print(now.strftime("%Y, %B, %d"))


name = "Hilman"

def printName():
	global name
	name = name + "bambang "
	print("akses dari dalam " + name)


printName()
print("dari luar" + name)