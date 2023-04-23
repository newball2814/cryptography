#!/usr/bin/python3

# Viet ham encode ROT13

s = input("s = ")

print("Ma hoa ROT13: ", end='')
def encode_rot13(s):
    res = ""
    for i in s: 
        if i.isalpha():
            res += chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
        else: 
            res += i

    return res

print(encode_rot13(s))


# b) Viet ham encode ROT47
#
# s2 = input("s = ")
#
# print("Ma hoa ROT47: ", end='')
# def encode_rot47(s2):
#     return "".join([chr((ord(i) + 14) % 94 + 33) for i in s2])
#
# print(encode_rot47(s2))
