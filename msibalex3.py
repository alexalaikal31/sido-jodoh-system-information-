import random
print("--- soal no 1 ---")
def alexalaikal():
    s = 10
    while s >= 0 :
        print(s)
        s-=1
        if(s==0):
            print("lets go")
alexalaikal()
print("--- soal no 2 ---")
def maximilian():
    cio = random.randint(1, 10)
    print('silakan tebak angka')
    while True:
        sad = int(input('\nMasukkan angka: '))
        if sad == cio:
            print('Selamat, tebakanmu benar!')
            break
        else:
            print('Tebakanmu terlalu','kecil'
                  if sad < cio
                  else 'besar'
                  )
maximilian()
    
