# -*- coding: utf-8 -*-
"""ba2a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uceUe_HVF2NYGnk9p2yVigXh-swvcqs5

**Implanted Motif Problem**

Implement MotifEnumeration (shown above) to find all (k, d)-motifs in a collection of strings.

Given: Integers k and d, followed by a collection of strings Dna.

Return: All (k, d)-motifs in Dna.
"""

def HammingDistance(p,q):
    n = len(p)
    counter = 0
    for i in range(0,n):
        if p[i] != q[i]:
            counter += 1
    return counter

def Neighbors(Pattern, d):  
    if d == 0:
       return [Pattern]
    if len(Pattern) == 1:
        return ['A','C','G','T']
    neighborhood = []
    suffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in suffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            neighborhood.append('A'+Text)
            neighborhood.append('C'+Text)
            neighborhood.append('G'+Text)
            neighborhood.append('T'+Text)
        else:
            neighborhood.append(Pattern[0] + Text)            
    return neighborhood

def MotifEnumeration(k, d, Dna):
    possibleMotifs = []
    for i in range(0,len(Dna)):
        # spremam sve susjede svih k-mera u jednom elementu liste (jednom retku) u all_neighb_in_row
        all_neighb_in_row = set()
        for j in range (0,len(Dna[i]) - k + 1):
            neighbors = Neighbors(Dna[i][j:j+k],d)
            for neighbor in neighbors:
                all_neighb_in_row.add(neighbor)
        # motivi su k-meri koji se pojavljuju kao susjedi nekog k-mera u svakom retku
        possibleMotifs.append(all_neighb_in_row)
    # motive trazim kao presjek svih skupova unutar possibleMotifs, jer su to k-meri koji se nalaze kao susjedi u svakom retku
    Motifs = possibleMotifs[0]
    for i in range(1, len(possibleMotifs)):
        Motifs = Motifs.intersection(possibleMotifs[i])
    return Motifs

f=open('rosalind_ba2a.txt')
lines=f.readlines()

k = int(lines[0].strip('\n').split(' ')[0])
d = int(lines[0].strip('\n').split(' ')[1])
Dna = []

for i in range(1,len(lines)):
   Dna.append(lines[i].strip('\n'))

def Output(array):

    out = ' '.join(array)
    print (out)

print(Output(MotifEnumeration(k,d,Dna)))