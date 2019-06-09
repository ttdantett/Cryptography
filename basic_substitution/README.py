# Basic substitution cipher 
#Usage example:

plaintext = "ilovecryptography"
_alphabet = "aqwzsxedcrfvtgbyhnujikolpm"
cipher = substitute(plaintext,_alphabet)
print(cipher)
plain = substitute(cipher,_alphabet,False)
print(plain)
