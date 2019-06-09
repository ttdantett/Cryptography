# Author: ttdantett
# Date: 09/06/2019

def create_substitution_table(_alphabet, enc):
	"""Creation of the substitution table"""
	d = {}
	# Original alphabet, can be changed
	alphabet = "abcefgdhijklmnopqrstuvwxyz"
	for i in range(len(_alphabet)):
		if enc:
		# Encryption table
			d[alphabet[i]] = _alphabet[i]
		else:
		# Decryption table
			d[_alphabet[i]] = alphabet[i]
	return d

def substitute(_plain, _alphabet, enc = True):
	"""Cipher for the encryption and decryption"""
	l = ""
	# Creation of the substitution table
	d = create_substitution_table(_alphabet, enc)
	# Result of the cipher
	for i in range(len(_plain)):
		try :
			# Add the corresponding characters from 
			# the new alphabet
			l += d[_plain[i]]
		except:
			# if a character not in the alphabet, 
			# will be replaced by a whitespace
			l += " "
	return l
