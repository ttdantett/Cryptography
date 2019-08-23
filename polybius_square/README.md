# Polybius square cipher 

| - | 1 | 2 | 3 | 4 | 5
| --- | --- | --- | --- | --- | --- |
| **1** | A | B | C | D | E |
| **2** | F | G | H | I | J |
| **3** | K | L | M | N | O |
| **4** | P | Q | R | S | T |
| **5** | U | V | W | X | Y |


## Usage example:

```python
cipher = encrypt("Thisisatest")
print(cipher)
```

```python
plain = decrypt(cipher)
print(plain)
```

## REMARK 
This polybius square does not let you use the character 'Z' in your plain text.
Please, don't use it in the plain text message.

