# list Comprehension 
myNumbers = [1,2,3,4,5,6,7,8,9]

doubledNumbers = []
for i in myNumbers:
    doubledNumbers.append(i*2)
print(f'using for: {doubledNumbers}')

doubledNumbers2 = [i*3 for i in myNumbers]
print(f'using for list: {doubledNumbers2}')

myName = 'Mahrokh'
nameChar = [i.upper() for i in myName]
print(nameChar)

print('=================================================')

newForTry =[i*2 if i%2==0 else i*3 for i in myNumbers]
print(newForTry)