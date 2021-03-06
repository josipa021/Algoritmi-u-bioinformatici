# -*- coding: utf-8 -*-
"""ba1l.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aiYVbu3UPB-F0sviEBj6xde8S3JSfm90
"""

def LastSymbol(pattern):
  return pattern[-1]

def Prefix(pattern):
   if(len(pattern)==1):
      return ""
   return pattern[0:-1]

def SymbolToNumber(symbol):
  if(symbol=='A'):
    return 0
  if(symbol=='C'):
    return 1
  if(symbol=='G'):
    return 2
  if(symbol=='T'):
    return 3

def PatternToNumber(pattern):
    if(pattern==""):
      return 0
    symbol=LastSymbol(pattern)
    prefix=Prefix(pattern)
    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)

pattern='TCACACTCCTTACGCCACTCTAGAAAGGGC'
print(PatternToNumber(pattern))