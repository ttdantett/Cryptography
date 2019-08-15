# Scytale encryption algorithme
# Author : ttdantett
# Date : 15/08/2019

from random import randint

# Scytale encryption 
alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# This is the size of the scytale, number of letters between the others
#size = 3

def scytale_encrypt(plain, size):
    cipher = ""
    for i in range(0, len(plain)):
        cipher += plain[i]
        for j in range(0, size):
            cipher += alphabet[randint(0,len(alphabet)-1)]
    return cipher

def scytale_decrypt(cipher, size):
    plain = ""
    for i in range(0, len(cipher), size + 1):
        plain += cipher[i]
    return plain
