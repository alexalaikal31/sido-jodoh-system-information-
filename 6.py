array = []
total = 0
n = int(input("Masukkan banyaknya elemen array: "))
for x in range(n):
    nilai = int(input("Masukkan nilai ke-{} : ".format(x+1)))
    array.append(nilai)
print(array)
tombol=input("tombol merah/biru : ")
if tombol=="merah":
    total=array[0]-1
    print(total)
elif tombol=="biru":
    total=array[0]*2
    print(total)
    
    print("\nHasil nilai total adalah : {}".format(sum(array)))
    print("Hasil rata-rata adalah : {}".format(sum(array)/n))
