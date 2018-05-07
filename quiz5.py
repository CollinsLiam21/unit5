#Liam Collins
#5/7/18
#quiz5.py

def penultimate(L):
    return L[-2]

def plusEquals(L,integer):
    new = []
    for item in L:
        new.append(item+integer)
    return new

def smallest(L):
    small = L[0]
    for item in L:
        if item < small:
            small = item
    return small