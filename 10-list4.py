# list Comprehension 
myNumbers = [1,2,3,4,5]

doubledNumbers = []
for i in myNumbers:
    doubledNumbers.append(i*2)
print(f'using for: {doubledNumbers}')

doubledNumbers2 = [i*3 for i in myNumbers]
print(f'using for list: {doubledNumbers2}')