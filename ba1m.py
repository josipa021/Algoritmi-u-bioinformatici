# -*- coding: utf-8 -*-
"""ba1m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E9VNNz3e8uRBCivw2XQ3uG4zTeB4xGqG

**Implement NumberToPattern**

Convert an integer to its corresponding DNA string.

Given: Integers index and k.

Return: NumberToPattern(index, k).
"""

def NumberToSymbol(num):

    if num == 0:
        return "A"
    if num == 1:
        return "C"
    if num == 2:
        return "G"
    if num == 3:
        return "T"

def NumberToPattern(index,k):

    if k == 1:
        return NumberToSymbol(index)

    remainder = index % 4
    index = index // 4
    pattern = NumberToPattern(index,k-1) 
    return pattern + NumberToSymbol(remainder)

print(NumberToPattern(8180,8))