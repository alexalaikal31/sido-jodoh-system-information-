class sepeda:
    def __init__(self, gigi, kecepatan):
        self.gigi = gigi
        self.kecepatan = kecepatan

    def Melaju(self):
        print("Melaju dengan kecepatan : ", self.kecepatan)

polygonxtrada = sepeda(3, 10)
polygonsierra = sepeda(4, 15)

print("gigi sepeda sebelumnya :",polygonxtrada.gigi)
print("gigi sepeda saat ini: ",polygonsierra.gigi)
polygonxtrada.Melaju()
polygonsierra.Melaju()
