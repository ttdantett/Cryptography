# Basic substitution cipher 
#Usage example:

plaintext = "ilovecryptography"
new_alphabet = "aqwzsxedcrfvtgbyhnujikolpm"
cipher = substitute(plaintext,new_alphabet)
print(cipher)
plain = substitute(cipher,new_alphabet,False)
print(plain)
