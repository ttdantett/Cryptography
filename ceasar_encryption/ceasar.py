# Ceasar cipher 
# Author : ttdantett 
# Date : 19/08/2019 

## Version 1
def encrypt(plain, rot):
    a = ""
    for i in plain:
        a += chr(ord(i) + rot % 26)
    return a

def decrypt(cipher, rot):
    a = ""
    for i in cipher:
        a += chr(ord(i) - rot % 26) # a remodif
    return a

## Version 2
def encrypt2(plain, rot):
    a = ""
    for i in plain.upper():
        a += chr(65 + (ord(i) - 65 + rot) % 26)
    return a

def decrypt2(cipher, rot):
    a = ""
    for i in cipher.upper():
        a += chr(65 + (ord(i) - 65 - rot) % 26)
    return a
