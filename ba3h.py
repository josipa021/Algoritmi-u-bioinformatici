# -*- coding: utf-8 -*-
"""ba3h.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13PmfqwY9bP1zuJX9qnT79FUlDNTg4QvZ

**String Reconstruction Problem**

Reconstruct a string from its k-mer composition.

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)
"""

def DeBruijn(Patterns,k):

    nodes = {}
    out = ""

    for i in range(0,len(Patterns)):
        
        prefix = Patterns[i][0:k-1]
        suffix = Patterns[i][1:k]
        
        if (prefix not in nodes.keys()):
            nodes[prefix] = [suffix]
        else:
            nodes[prefix].append(suffix)

    for prefix in nodes.keys():
        out += prefix + " -> "
        for suffix in sorted(nodes[prefix]):
            out += suffix + ","
        out = out.strip(",") #mičem zadnji zarez
        out += "\n"

    return out

def rosalindInputToGraph(text):
    
    dictionary = {}
    
    for line in text:
        key, values = line.split(" -> ")
        values = values.split(",")
        dictionary[key] = values
        
    return dictionary

def eulerianCycle(graph):
    
    cycle = [list(graph.keys())[0]]
    
    while (len(graph) > 0):

        if cycle[0] == cycle[-1]:

            while not cycle[0] in graph:
                cycle.pop(0)
                cycle.append(cycle[0])
          
        start = cycle[-1]
        
        cycle.append(graph[start].pop())  
        if len(graph[start]) == 0: del graph[start]
       
    return cycle

def eulerianPath(graph):

    # find the unbalanced nodes
    balances = {}

    # set values of all nodes in graph to 0
    for key in graph.keys():
        for element in graph[key]:
            if element not in balances.keys():
                balances[element] = 0
        if key not in balances.keys():
            balances[key] = 0
    
    for sourceNode in graph.keys():
        for targetNode in graph[sourceNode]:

            # finding the difference between indegree and outdegree:
            # +1 for every time you enter this node ( -> node)
            balances[targetNode] += 1
            # -1 for every time you leave this node ( node -> )
            balances[sourceNode] -= 1
            
    
    for node in balances:

        # if you can leave a node but can't enter it:
        if balances[node] == -1:
            targetNode = node
        # if you can enter a node but can't leave it:
        if balances[node] == 1:
            sourceNode = node

    # add the missing edge
    if sourceNode in graph.keys():
        graph[sourceNode].append(targetNode)
    else:
        graph[sourceNode] = [targetNode]

    # run eulerianCycle and drop the circle closing postfix
    path = eulerianCycle(graph)[0:-1]

    # rotate until the missing edge matches end and beginning
    while path[0] != targetNode or path[-1] != sourceNode:  
       path.append(path.pop(0))
       
    return path

def Output(res):

    out = res[0]
    
    for i in range(1,len(res)):
        out += res[i][-1]

    print (out)

f=open('rosalind_ba3h.txt')
lines=f.readlines()

k = int(lines[0].strip('\n'))
Patterns = []

for i in range(1,len(lines)):
    Patterns.append(lines[i].strip('\n'))
    

graph = DeBruijn(Patterns, k).strip('\n')
graph = graph.split('\n')
graph = rosalindInputToGraph(graph)
res = eulerianPath(graph)

Output(res)