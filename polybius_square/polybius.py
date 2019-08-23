# Polybius square 
# Author: ttdantett
# Date: 23/08/2019

def polybius_table():
    pol_dic = {}
    for i in range(0,5):
        for j in range(0,5):
            charac = chr(65 + i * 5 + j % 5)
            pol_dic[charac] = str(j) + str(i)
    return pol_dic

def reverse_polybius():
    pol_dic = polybe_table()
    rev_dic = dict((pol_dic[k], k) for k in pol_dic)
    return rev_dic

def encrypt(plain):
    pol_dic = polybius_table()
    enc = ""
    for i in plain.upper():
        enc += pol_dic[i]
    return enc

def decrypt(cipher):
    rev_dic = reverse_polybius()
    dec = ""
    for i in range(0, len(cipher) - 1, 2):
        dec += rev_dic [cipher[i] + cipher[i+1]]
    return dec
