'ABC'.join(['Dicoding', '', 'Indonesia'])

list_a = range(1,10,2)
x = [ [a**2, a**3] for a in list_a]
print(x)
for i in range(0, 5):
    for j in range(0, 5 - i):
        print('*', end='')
    print()

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)
var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)

for i in range(0, 5):
    for j in range(0, 5 - i):
        print('*', end='')
    print()

from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print ('{}(a, b): {}'.format(func.__name__, func(a, b)))
s = "Hello World!"
print(s)
s= "Try Python!"
print(s)

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);

name = "John"
age = 15
print("%s is %d years old." % (name, age))

a, b = 10, 11
a, b
print('a: %x and b: %X' % (a, b))

a = 6
b = 4
print("Hasilnya " + str (a + b) + "6" * 3)
uang = 500000
bonus = 1.1
hasil = uang + (bonus ** 6)
print("Jumlah uang selama 6 bulan adalah", hasil)

print("Hello" + 3)
p = 'Hello world!'
p = p.upper()
print(p)

feeling = input('How are you?')
if feeling.lower() == 'great':
    
    'Hello'.rjust(20)
    #spam = '    Hello World     '
    #spam.strip()
    #print(spam)
    print('I feel great too.')
    string = "Ayo belajar Coding di Dicoding"
    print(string.replace("Coding", "Pemrograman"))
else:
    print('I hope the rest of your day is good.')

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
for i in range(3, 9):
    print(i)
y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
y.sort()
print(y)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
arr = [0]*10
len(arr)
print(arr)
s = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''.split('\n')
print(s)
#import sys
#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
#print(sys.argv[1])
