#!/usr/bin/python3

key = [9, 13]
# text = 'PER ASPERA AD ADSTRA'
text = 'cjh vxl blx yljap uhxc anr'

# Encryption 
def encrypt(text, key):
    return ''.join([chr((key[0]*(ord(t) - 65) + key[1] ) % 26 + 65) for t in text.upper().replace(' ', '')])

# Modulo inverse
def inverse(A, M):
    m0 = M
    y = 0
    x = 1

    if (M == 1):
        return 0

    while (A > 1):
        q = A // M

        t = M

        M = A % M
        A = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0
        
    return x

# # Decryption 
# def decrypt(ctext, key):
#     return ''.join([ chr((( inverse(key[0], 26)*(ord(c) - ord('A') - key[1]))
#                     % 26) + ord('A')) for c in ctext ])
#

# Decrypt  
def decrypt(cipher_text, a, b): 
  
    # Calculate the inverse of a 
    a_inv = 0
    for i in range(1, 26): 
        if (a * i) % 26 == 1: 
            a_inv = i 
  
    # Initialize the plain text 
    plain_text = "" 
  
    # Decrypt the cipher text 
    for c in cipher_text: 
        if c.isalpha(): 
            plain_text += chr((inverse(a, 26) * (ord(c) - ord('A') - b)) % 26 + ord('A')) 
        else: 
            plain_text += c 
  
    # Return the plain text 
    return plain_text 

if __name__ == "__main__":
    print("Encrypted message: {}".format(encrypt(text, key)))
    # print("Decrypted message: {}". format(decrypt(encrypt(text, key), key)))
    # print(decrypt(text, key[0], key[1]))
