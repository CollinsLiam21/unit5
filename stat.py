#Liam Collins
#4/26/18
#stat.py

L = []
while True:
    nums = input('Enter a list of numbers, Type q when finished: ')
    if nums != 'q':
        L.append(float(nums))
    else:
        break

for item in L:
    print(item)

print('Min: ', max(L))
print('Mean: ', sum(L)/(len(L)))
print('Max: ', min(L))

christo = 0
for item in L:
    if L.count(item) > L.count(christo):
        christo = item
print('Mode: ', christo)

L.sort()
if len(L.sort())%2 == 0:
    print(L[(len(L.sort())/2)-1],L[(len(L.sort())/2)])
else:
    print(L[len(L.sort())//2])




