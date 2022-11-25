import random
import operator
import functools
from utils import *

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  #Kis prímek
mul_small_primes = functools.reduce(operator.mul, small_primes) # szorzat = 6469693230

def check_len(q, desired_size):
    return len(bin(q)) - 2 == desired_size

def isprime(a): #Prímteszt
    if a%2 == 0:
        return False
    i=3
    while a>=i*i:
        if a%i == 0:
            return False
        i+=2
    return True

def gen_odd_q(size):  #random páratlan szám 2 hatvány, tehát nem számjegy a méret
    q = random.randint(2 ** (size - 1), 2 ** size - 1)
    if q & 1 == 0:
        q += 1
    return q

def gen_relatively_prime(size): #relatív prím készítése
    q = gen_odd_q(size)
    while gcd(q, mul_small_primes) > 1 or q % 4 != 3:
        q += 2
        if not check_len(q, size):
            q = gen_odd_q(size)
    return q

def gen_prime(size): #random prímszámot ad vissza, a méret itt is 2 hatvány
    diff = 2
    q = gen_odd_q(size)
    if size > 50:
        q = gen_relatively_prime(size)
        diff = mul_small_primes
    while not isprime(q) or q % 4 != 1:
        q += diff
    return q




