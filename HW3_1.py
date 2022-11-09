# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:46:17 2020

@author: Kasia
"""

import string
alphabet = " " + string.ascii_lowercase

positions = dict.fromkeys(alphabet, 0)
for i,c in enumerate(alphabet):
    positions[c] = i
    
message = "hi my name is caesar"
encoded_message = ""
for i,c in enumerate(message):
    number = positions[c]
    if number == 26:
        encoded_message += list(positions.keys())[list(positions.values()).index(0)]
    encoded_message += list(positions.keys())[list(positions.values()).index(number + 1)]

def encoding(message, key):
    cipher = ""
    for i,c in enumerate(message):
        number = positions[c]
        #if number > 26 - key:
        cipher += list(positions.keys())[list(positions.values()).index((number + key)%27)]
        """elif (key < 0 and number < -key):
            cipher += list(positions.keys())[list(positions.values()).index(-key)]
        elif number <=26:
            cipher += list(positions.keys())[list(positions.values()).index(number + key)]"""
    return cipher

encoded_message = encoding(message, key = 3)
print(encoded_message)

print(encoding(encoded_message, key = 24))