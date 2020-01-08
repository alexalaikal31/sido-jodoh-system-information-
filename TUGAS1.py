import random
print("*******WELCOME DI APLIKASI SAMPEL KECOCOKAN CINTA*******")
for a in range(5,1,-1):
    for b in range(a,2,-1):
        print(' ', end=' ')
    for c in range(6,a,-1):
        print('P', end=' ')
    for d in range(6,a,-1):
        print('U', end=' ')
    for e in range(a,2,-1):
        print(' ', end=' ')
    for f in range(a,2,-1):
        print(' ', end=' ')
    for g in range(6,a,-1):
        print('T', end=' ')
    for h in range(6,a,-1):
        print('u', end=' ')
    print()

for k in range(1,10):
    for l in range(1,k):
        print(' ', end=' ')
    for m in range(9,k,-1):
        print('S', end=' ')
    for n in range(9,k,-1):
        print('s', end=' ')
    for o in range(1,k):
        print(' ', end=' ')
    print()
baleni = True
while baleni:
    print("| MULAI |")
    S = input("YA / NO")
    if S == "YA":
        baleni = False 
        print("Loading...")
        cowok = input("Masukkan nama laki: ")
        usia = int(input("Masukkan Usia: "))
        print("|SAMPEL COWOK|")
        print("| NAMA |",cowok,"|")
        print("| USIA |",usia,"|")
        cewek = input("Masukkan nama wanita: ")
        usek = int(input("Masukkan Usia: "))
        print("|SAMPEL CEWEK|")
        print("| NAMA |",cewek,"|")
        print("| USIA |",usek,"|")
        if usia == 25 and usek == 21:
            print("karakter")
            print("| PRIA | PEMAHAMAN | SETIA | PRESTASI |" )
            cora1 = random.randrange(36,69)
            cora2 = random.randrange(36,69)
            cora3 = random.randrange(36,69)
            cera3 = random.randrange(36,69)
            cera1 = random.randrange(36,69)
            cera2 = random.randrange(36,69)
            print("| ",cowok," | ",cora1," | ",cora2," | ",cora3," | ")
            print("| WANITA | PEMAHAMAN | SETIA | PRESTASI |")
            print("| ",cewek," | ",cera1," | ",cera2," | ",cera3," | ")
            DNA = cora1 + cora2 + cera1 + cera2 + cera3 + cora3 / 100
            print(" TINGKAT KECOCOKAN = ",round(DNA))
            if DNA > 200:
                print(" SESUAI KELUARGA BERENCANA ")
            elif DNA > 130:
                print(" PIKIR KERI ")
            else:
                print(" KUATKAN IMAN ")
        elif usia >= 25 and usek >= 21:
            print("karakter")
            print("| PRIA | PEMAHAMAN | SETIA |")
            cora1 = random.randrange(70,100)
            cora2 = random.randrange(70,100)
            cora3 = random.randrange(70,100)
            cera3 = random.randrange(70,100)
            cera1 = random.randrange(70,100)
            cera2 = random.randrange(70,100)
            print("| ",cowok," | ",cora1," | ",cora2," | ",cora3," | ")
            print("| WANITA | PEMAHAMAN | SETIA | PRESTASI |")
            print("| ",cewek," | ",cera1," | ",cera2," | ",cera3," | ")
            DNA = cora1 + cora2 + cera1 + cera2 + cera3 + cora3 / 100
            print(" TINGKAT KECOCOKAN = ",round(DNA))
            if DNA > 300:
                print(" MANTAP BERUMAH TANGGA ")
            elif DNA > 200:
                print(" RAWAN PERTENGKARAN ")
            else:
                print(" PERANG DUNIA KE 3 ")
        elif usia <= 25 and usek <= 21:
            print("karakter")
            print("| PRIA | PEMAHAMAN | SETIA |")
            cora1 = random.randrange(0,35)
            cora2 = random.randrange(0,35)
            cora3 = random.randrange(0,35)
            cera3 = random.randrange(0,35)
            cera1 = random.randrange(0,35)
            cera2 = random.randrange(0,35)
            print("| ",cowok," | ",cora1," | ",cora2," | ",cora3," | ")
            print("| WANITA | PEMAHAMAN | SETIA | PRESTASI |")
            print("| ",cewek," | ",cera1," | ",cera2," | ",cera3," | ")
            DNA = cora1 + cora2 + cera1 + cera2 + cera3 + cora3 / 100
            print(" TINGKAT KECOCOKAN = ",round(DNA))
            if DNA > 65:
                print(" MULUT DIAM HATI BERKATA KATA ")
            elif DNA > 30:
                print(" RAWAN PLAYBOY ")
            else:
                print(" BELUM ADA PANDANGAN ")
        else:
            print("WOW jodoh anda terlalu tinggi kriterianya")

