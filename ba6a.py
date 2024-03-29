# -*- coding: utf-8 -*-
"""ba6a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ROzr5ygf6gwe_gp2zgmDHFA8hK549Xvf

**Implement GreedySorting**

Given: A signed permutation P.

Return: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.
"""

def changeSign(number):

    if number[0] == '+':
        number = number.replace('+','-')
    else:
        number = number.replace('-','+')

    return number

def reverse(permutation, start, end):

    rev_segment = []
    segment = permutation[start:(end + 1)]
    new_permutation = []
    
    for i in range(len(segment)-1,-1,-1):

        rev_segment.append(changeSign(segment[i]))

    new_permutation = permutation[:start] + rev_segment + permutation[end+1:]

    return new_permutation

def rosalindOutput(permutations):

    out = []
    
    for p in permutations:

        line = '(' + ' '.join(p) + ')'
        out.append(line)

    return '\n'.join(out)

def GreedySorting(P):

    n = len(P)
    permutations = []

    '''
    "i" određuje broj u permutaciji
    u svakom koraku stavimo element na i-toj poziciji na pravo mjesto tako da u sljedećem
    koraku za traženje broja uzimamo samo segment izmedu trenutne pozicije i tog broja(taj broj je sigurno
    desno od trenutne pozicije jer su lijevo svi vec poslozeni)
    '''
    for i in range(1,n+1):

        if P[i-1][1:] != str(i):

            '''reverse the segment between the current position and the position
                of the number that should be in current position'''
            for j in range(i,n):
                if P[j][1:] == str(i):
                    P = reverse(P,i-1,j)
                    permutations.append(P)
                    break

        if P[i-1][0] == '-':
            P = reverse(P,i-1,i-1)
            permutations.append(P)

    return rosalindOutput(permutations)

f=open('rosalind_ba6a.txt')
line=f.readline()

P = line[1:(len(line)-2)] #excluding ")" and "\n"
P = P.split(' ')

print(GreedySorting(P))