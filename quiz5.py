#


def penultimate(L):
    return L[1:]

def plusEquals(L,integer):
    for item in L:
        item = item + integer

def smallest(L):
    small = L[0]
    for item in L:
        if item < small:
            small = item
    return small