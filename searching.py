"""
Created on Mon Oct 28 16:26:42 2019

@author: alial
"""
def linear_search(l, item, issorted=False):
    #if issorted == False:
    #    l = l.sort()
    for i in range(len(l)):
        if l[i] == item:
            return i
    return None

def binary_search(l, item, issorted=False):
    #if issorted == False:
    #    l = l.sort()
    if issorted:
        i = 0
        j = len(l) - 1
        while i!= j + 1:
            middle = (i + j) // 2
            if l[middle] < item:
                i = middle + 1
            else:
                j = middle - 1
        if (l[i] == item):
            return i
        else:
            return None
    else:
        d = {}
        for (i, value) in enumerate(l):
            d[value] = i
        listSorted = l.copy()
        listSorted.sort()
        i = 0
        j = len(listSorted) - 1
        while i!= j + 1:
            middle = (i + j) // 2
            if listSorted[middle] < item:
                i = middle + 1
            else:
                j = middle - 1
        if (0 <= i < len(listSorted)) and (listSorted[i] == item):
            return d[item]
        else:
            return None
