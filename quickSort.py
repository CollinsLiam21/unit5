#Liam Collins
#5/2/18
#sortingTemplate.py - times a sorting function

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A,lo,hi):
    if lo < hi:
        p = partition(A,lo,hi)
        quicksort(A,lo,hi)
        quicksort(A,p+1,hi)

def partition(A,lo,hi):
    pivot = A[lo]
    i = lo - 1
    j = hi + 1
    while True:
        i = i + 1
        while A[i] < pivot:
            j = j - 1
        while A[j] > pivot:
            if i >= j:
                return j
        A[i], A[j] = A[j], A[i]
        
            
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    #numbers = numbers.sort()
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
