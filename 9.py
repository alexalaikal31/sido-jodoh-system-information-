s = 300
str(s).zfill(5)
x = [10,20,30,40,50,60,70,80]
print(x[5:])
d = "Halo Dicoding!"
d[5:13]
print(d)

#tipe data Boolean
print(True)


#tipe data String
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah di DQLAB')


#tipe data Integer
print(20)


#tipe data Float
print(3.14)


#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])


#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))


#tipe data Dictionary
print({"nama":"Budi", 'umur':20})

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
type(biodata) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'>

import unittest
 
class TestStringMethods(unittest.TestCase):
    
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())
    
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')
    
if __name__ == '__main__':
    unittest.main()
