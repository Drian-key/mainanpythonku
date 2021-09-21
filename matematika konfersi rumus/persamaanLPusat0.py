
#input angka


#persamaan lingkaran yang berpusat di O(0, 0) dan diketahui jari jari
def DiketR():
    r = int(input("masukan jari-jari: "))
    print("x^2 + Y^2 = r^2")
    print("x^2 + Y^2 = " + str(r) + "^2")
    print("x^2 + Y^2 = " + str(r**2) )

#persamaan lingkaran jika diketahui pusatnya 
def DiketM():
    r = [int(input("x: ")), int(input("y: "))]
    xy = r[0]**2 + r[1]**2
    print("(" + str(r[0]) + ")^2 + (" + str(r[1]) + ")^2 = r^2")
    print(str(r[0]**2) + " + " + str(r[1]**2) +  " = r^2")
    print(str(xy) +  " = r^2")
    print("x^2 + Y^2 = " + str(xy))

def DiketP():
    


