import random

from params import p
from params import g

def keygen():

    sk = random.randrange(2,p)  #a
    pk = pow(g, sk, p)          #h

    return pk,sk

def encrypt(pk,m):

    r = random.randrange(2,p)

    c1 = pow(g, r, p)
    c2 = (m * pow(pk, r, p)) % p
    return [c1,c2]

def decrypt(sk,c):

    c1, c2 = c
    m = c2 * pow(c1, -sk, p) % p

    return m

