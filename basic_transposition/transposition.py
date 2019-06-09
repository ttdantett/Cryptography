# Author: ttdantett
# Date: 09/06/2019

def create_transposition_table(_key, enc):
	"""Creation of the transposition table"""
	# Creation of a table containing a tuple (key, index)
	l = []
	m = [''] * len(_key)
	for i in range(len(_key)):
		l.append((_key[i], i))
	# Sort the  table
	l.sort()
	for i in range(len(l)):
		#if encryption
		if enc:
			m[l[i][1]] = i
		# if decryption
		else:
			m[i] = l[i][1]
	return m

def transpose(_text, _key, enc = True):
	"""Transposition, encryption by default"""
	if enc:
		# Padding of the table for the encryption
		l = len(_key) - (len(_text)%len(_key))
		for i in range(l):
			_text += ' '
	# Creation of the variable
	t = [' '] * len(_text)
	# Creation of the table 
	table = create_transposition_table(_key,enc)
	result = ""
	# Transposition of the table
	for i in range(len(_text)):
		if enc:
		 # Encryption 
			t[int((i/len(_key))) + int(table[int(i%len(_key))]*(len(_text)/len(_key)))] = _text[i]
		else:
		# Decryption
			t[(i%int(len(_text)/len(_key)))*len(_key) + table[int(i/(len(_text)/len(_key)))]] = _text[i]
	# Creation of the string
	for i in range(len(_text)):
		result += t[i]

	return result
