#Liam Collins
#4/25/18
#dictionaryDemo.py - more list practice 

words = ['computer','mortify','dog','firetruck','yes','python','cat']

words.sort()

num = int(input('What number word do you want? '))
if num<=0 or num>=len(words)+1:
    print('Invalid Number')
else:
    print(words[num-1])
