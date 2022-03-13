# -*- coding: utf-8 -*-
"""ba1d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xm-dlNlywgwnZKBoCKln0ZJGjPHXWGwc

Pattern Matching Problem:

Find all occurrences of a pattern in a string.

Input: Strings Pattern and Genome.

Output: All starting positions in Genome where Pattern appears as a substring
"""

def Func(pattern,genome):
  n=len(pattern)
  lista=[]
  if(n<=len(genome)):
    for i in range (0,len(genome)-n+1):
      if(genome[i:i+n]==pattern):
        lista.append(i)
  return lista

pattern=''
genome=''

print(Func(pattern,genome))