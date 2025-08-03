#def Sadhu():
#    print("Menjumlah dua buah bilangan")
#    Max = int(input("bilangan pertama:"))
#    Cio = int(input("Bilangan kedua:"))
#    print("jumlah = ", (Max + Cio))

#Sadhu()

#def ditinggalmantan():
#    a_dict = {'nama':'Maximilian Prawiro','umur':'13 Tahun','tgl lahir':'1 Desember 2008','almamater':'Sekolah Benih Harapan','hobi':'basket','alamat':'jalan nusantara GG5 perumahan Kaliwates Jember','mapel':'fisika','makanan':'pecel','anjing':'moci','adik':'gwen'}
#    for gwen in a_dict:
#        del a_dict[gwen]
#        print(gwen,' = ', a_dict[gwen])
#ditinggalmantan()

#a_dict = {'John': 32, 'Mel': 31, 'Nik': 33, 'Katie': 32, 'James': 29, 'Matt': 35}
import json
#sadhu = 'aku bilang "kalau aku" benci kamu'
#max_string = 'aku'
#temp_str = sadhu.lower()
#count = temp_str.count(max_string.lower())
#print(count)



#import collections
#string='saya mau berkata saya mau pergi kepada paman saya'
#us=string.lower()
#li=us.split(' ')
#ambil=collections.Counter(li).most_common()
#for kata in ambil:
    #print("%s\t: %d"%(kata[0],kata[1]))
#data_JSON = json.dumps(ambil)
#print(data_JSON)
#type(data_JSON)
#data_max = {"nama":"maximilian prawiro","umur":"13","kota":"jember"}
#data_JSON = json.dumps(data_max)
#print(data_JSON)
#type(data_JSON)


class Mobil:
    merk = ""
    warna = ""

    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def tampilkan_info(self):
        print("mobil dengan merk " + self.merk + " berwarna " + self.warna)

mobil1 = Mobil("toyota", "merah")
mobil1.tampilkan_info()
mobil1 = Mobil("suzuki", "biru")
mobil1.tampilkan_info()

mobil1 = Mobil("honda", "merah")
print(mobil1.merk)
mobil1.merk = "yamaha"
print(mobil1.merk)


class Mobil2:

    def __init__(self, roda, tipe, kecepatan):
        self.tipe = tipe
        self.roda = roda
        self.kecepatan = kecepatan

    def doMelaju(self):
        print("Melaju dengan kecepatan : ", self.kecepatan)
    
    def doKlakson(self):
        print("klakson")

    def doBelok(self, arah):
        print("Belok arah ", arah)

mobilFerari = Mobil2("Sport", 4, 200)
mobilJeep = Mobil2("Offroad", 6, 150)

print(mobilFerari.tipe)
print(mobilJeep.tipe)
mobilFerari.doMelaju()
mobilJeep.doMelaju()

num = 10
for num in range (1):
    num = num - 1
    print(num)

x = [3,2]
y=0
y,x[y] = 1,8
print(x)

result = False and (False or (True and (not False)))
print(result)

myList = ['n','b','a','c','b','a']
mySet = set(myList)
myTuple = tuple(mySet)
print(myTuple)

print('JavaScript'[2:5])
print('G'in'Good')
print('A'not in 'Good')
print('g'in'Good')
print('g'not in'Good')

num = 340.56436
print("Float Value is: %.2f " %num)

def fungsi1(num):
    return num*10
def fungsi2(num):
    return num*20
def fungsi3(num):
    return num*30
result = fungsi1(1)+fungsi2(2)+fungsi3(3)
print(result)

x=0
while(x<100):
    x+=2
print(x)

numbers = [10,20]
items = ["chair","table"]
for x in numbers:
    for y in items:
        print(x,y)


class Dog:
    def walk(self):
        return "walking"
    def speak(self):
        return "woof"
class JackRussellTerrier(Dog):
    def speak(self):
        return "arrf!"
bang = JackRussellTerrier()
bang.speak()

datamax = {
    "name":"max",
    "age":14,
    "score":{
        "fisika":80,
        "matematika":10,
        "bahasa bali":70,
        "bahasa osing":40
        }
    }
datamax["score"]["matematika"]

m = 0
a = 0
x = -5
if a > 0:
    if x < 0:
        m = m + 5
    elif  a > 5:
        m = m + 4
    else:
        m = m + 3
else:
    m = m + 2
print(m)

letter = "alex"
for letter in 'AI Talents':
    if letter.lower() in "auieo":
        pass
    else:
        print(letter, end='')

riski = [s for s in range(1,10)if s%2==0]
print(riski)
