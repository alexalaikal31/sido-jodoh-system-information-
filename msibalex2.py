def Pengurangan():
    first_number = int(input("bilangan pertama:"))
    second_number = int(input("bilangan kedua:"))
    print("jumlah = ", (first_number - second_number))

def Perkalian():
    first_number = int(input("bilangan pertama:"))
    second_number = int(input("bilangan kedua:"))
    print("jumlah = ", (first_number * second_number))

def Pembagian():
    first_number = int(input("bilangan pertama:"))
    second_number = int(input("bilangan kedua:"))
    print("jumlah = ", (first_number / second_number))

def hasil():
    first_number = int(input("bilangan pertama:"))
    second_number = int(input("bilangan kedua:"))
    c = first_number * second_number
    if (c >50):
        print("jumlah lebih = ",c)
    elif (c<50):
        print("jumlah kurang = ",c)
    elif (c!=25):
        print("jumlah bukan 25 = ",c)
    

Pengurangan()
Perkalian()
Pembagian()
hasil()

    
