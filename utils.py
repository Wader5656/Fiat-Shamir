import sys
import random


def read(filename):
    with open(filename) as f:
        return int(f.read())

def read_mul(*filenames):
    return (read(arg) for arg in filenames)

def read_struct(filename):
    if not filename:
        print('Nincs ilyen fájl: {}'.format(filename))
        exit(1)
    with open(filename) as f:
        return eval(f.read())


def read_bin(filename):
    with open(filename, 'rb') as f:
        return f.read()


def write(filename, value):
    with open(filename,'w') as f:
        f.write(str(value))
#Eddig csak fájlkezelés, ami miatt átláthatóbb a main



def gcd(x, y):  #Legnagyobb közös osztó
    x, y = max(x, y), min(x, y)
    while y:
        x, y = y, x % y
    return x

def egcd(a, b):   #kibővített euklideszi algoritmus
    r0, r1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    q, r2 = r0 // r1, r0 % r1
    while r2 != 0:
        x1, x0 = x0 - q * x1, x1
        y1, y0 = y0 - q * y1, y1
        r1, r0 = r2, r1
        q, r2 = r0 // r1, r0 % r1
    return r1, x1, y1


def get_inverse(a: int, m: int):  #moduláris inverz
    if a == 0:
        return 0
    d, x, y = egcd(a, m)
    return x % m

def get_bits(e: int, count=-1):  #2-es számrendszerre alakítás
    return [int(bit) for bit in bin(e)[2:count]]



    


