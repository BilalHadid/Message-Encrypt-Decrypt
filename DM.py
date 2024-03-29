# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:00:43 2019

@author: bilal
"""

# encrypt and decrypt a text using a simple algorithm of offsetting the letters

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

#text = "I am coding Python on SoloLearn!"
text=str(input("ENTER THE MESSAGE"))      
offset = 5

encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)

decrypted = decrypt(offset, encrypted)
print('Decrypted:', decrypted)