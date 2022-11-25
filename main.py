#Futtatás: main.py -gp (alapértelmezetten van megadva 30 és 10 értékeknek, de 2 paraméter megadásával ez változtatható)
#         main.py -gp  main.py -gk , main.py -s és main.py -c a sorrend
#Illetve létezni kell az összes txt-nek, nem hozza létre magának a program.
#A ds.txt-ben bármi nemű változás esetén a tesztelés "Not equal" értéket ír ki a kimenetre

from utils import *
import prime
import hashlib
import sys

DEFAULT_PQ_SIZE = 30
DEFAULT_KEY_SIZE = 10
mysha = hashlib.sha256
f = open('n.txt','r+')
g = open('k.txt','r+')
h = open('s_key.txt','r+')
j = open('v_key.txt','r+')
l = open('co.txt','r+')


def gen_params(pq_size, k):    #n és k értékek generálása 2 prímmel
    p = prime.gen_prime(pq_size)
    q = prime.gen_prime(pq_size)
    n = p * q
    f.write(str(n))
    g.write(str(k))

def gen_keys(n, k):  #Aláíró és ellenőrző kulcsok generálása
    s = []
    while len(s) < k:
        si = random.randint(1, n - 1)
        if prime.gcd(si, n) == 1:
            s.append(si)
    v = [pow(get_inverse(si, n), 2, n) for si in s]
    h.write(str(s))
    j.write(str(v))

def sign(n, k,sk): #Aláírás, sha256-os hash-el
    r = random.randint(1, n - 1)
    u = pow(r, 2, n)
    e = mysha(u.to_bytes(len(bin(u)) - 2, byteorder='big')).digest()
    e = int.from_bytes(e, byteorder='big')
    ek = get_bits(e, k)
    s = r
    for (si, ei) in zip(sk, ek):
        s = s * pow(si, ei, n) % n
    l.write(str((e, s)))


def check(ds, n, k, v): #ellenőrzés, szintén sha256-al
    e, s = ds
    ek = get_bits(e, k)
    w = pow(s, 2, n)
    for (vi, ei) in zip(v, ek):
        w = w * pow(vi, ei, n) % n
    es = mysha(w.to_bytes(len(bin(w)) - 2, byteorder='big')).digest()
    es = int.from_bytes(es, byteorder='big')
    if e == es:
        print('Equal')
    else:
        print('Not equal')

def main():
    operation = sys.argv[1]
    if operation == '-gp':
        gen_params(int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) == 4 else gen_params(DEFAULT_PQ_SIZE,DEFAULT_KEY_SIZE)
    elif operation == '-gk':
       gen_keys(*read_mul('n.txt', 'k.txt'))
    elif operation == '-s':
        sign(*read_mul('n.txt', 'k.txt'), read_struct('s_key.txt'))
    elif operation == '-c':
        check(read_struct('co.txt'), read('n.txt'), read('k.txt'), read_struct('v_key.txt'))

    

if __name__ == "__main__":
    main()