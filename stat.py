#Liam Collins
#4/26/18
#stat.py

L = []
while True:
    nums = input('Enter a list of numbers, Type q when finished: ')
    if nums != 'q':
        L.append(nums)
    else:
        break

for item in L:
    print(item)
print('The max is:', min(L))
print('The min is:', max(L))




