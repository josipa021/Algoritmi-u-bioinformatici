# -*- coding: utf-8 -*-
"""ba3c.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ENIKVwrFZ7jsI0ec760vS3KJrou_N_H6

**Overlap Graph Problem**

Construct the overlap graph of a collection of k-mers.

Given: A collection Patterns of k-mers.

Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
"""

def OverlapGraph(Patterns):
    overlaps = ""
    k = len(Patterns[0]) # patterns je lista k-mera
    for i in range (0,len(Patterns)-1):
        for j in range(i+1,len(Patterns)):
            # odmah se vrsi provjera
            if (Patterns[i][1:k] == Patterns[j][0:k-1]):
                 overlaps += Patterns[i] + " -> " + Patterns[j] + "\n"     
            if (Patterns[j][1:k] == Patterns[i][0:k-1]):
                overlaps += Patterns[j] + " -> " + Patterns[i] + "\n"              
    return overlaps

f=open('rosalind_ba3c.txt')
lista=f.readlines()

for i in range(0,len(lista)):
  lista[i]=lista[i].strip("\n")

print(OverlapGraph(lista))