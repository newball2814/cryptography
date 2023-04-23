#!/usr/bin/python3 

def gcd(a, b):
    while (b):
        a, b = b, a % b 
    return abs(a)

p = int(input("p = "))
q = int(input("q = "))
m = int(input("m = "))

e = 2
n = p * q
phi = (p - 1) * (q - 1)

# Encryption

# Check co-prime
while (e < phi):
    if gcd(e, phi) == 1:
        break
    else:
        e = e + 1

c = (m ** e) % n

# Decryption
def mod_inverse():
    for i in range(1, phi):
        if (((e % phi) * (i % phi)) % phi == 1):
            return i 
    return -1

m = (c ** mod_inverse()) % n

# Main
print("Encrypted text: {}".format(c))    
print("Decrypted text: {}".format(m))
