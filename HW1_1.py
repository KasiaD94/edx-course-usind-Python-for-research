# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:21:19 2020

@author: Kasia
"""

sentence = 'Jim quickly realized that the beautiful gowns are expensive'
def counter(input_string):
    unique_letters = list(set(input_string))
    print(unique_letters)

    count_letters = dict.fromkeys(unique_letters, 0)

    for letter in input_string:
        count_letters[letter] = count_letters[letter] + 1
        
    return (count_letters)

counter(sentence)