# -*- coding: utf-8 -*-
"""ba3b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t_Ff6anTc-EJ09TeDfaNHQmPiluPCtty

**String Spelled by a Genome Path Problem**

Find the string spelled by a genome path.

Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.

Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.
"""

def StringFromGenomePath(sequence):
    string = sequence[0] # cili prvi element od sequence
    for i in range(1,len(sequence)):
        # zadnji znak u svakon el. od sequence (pocevsi od drugog)
        string += sequence[i][len(sequence[i])-1]
    return string

f=open('rosalind_ba3b.txt')
lista=f.readlines()

for i in range(0,len(lista)):
  lista[i]=lista[i].strip("\n")

print(StringFromGenomePath(lista))