#Liam Collins
#4/26/18
#vowelWordsDemo.py

words = input('Enter list of words: ').split(' ')

for item in words:
    if item[0] in 'aeiouAEIOU':
        print(item)
