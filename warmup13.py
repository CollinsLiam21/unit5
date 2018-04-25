#Liam Collins
#4/25/18
#warmup13.py

from random import randint

L = []
for i in range(1,21):
    L.append(randint(1,100))

print(sum(L))
print(max(L))
print(min(L))
