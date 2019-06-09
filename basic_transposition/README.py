# Basic transposition cipher 

Usage example:

plaintext = "ilovecryptography"
key = "secret"
cipher = transpose(plaintext,key)
print(cipher)
plain = transpose(cipher,key,False)
print(plain)
