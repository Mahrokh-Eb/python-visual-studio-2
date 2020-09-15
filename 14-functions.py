def print_squre_of_7(): 
    print(7*7)
print_squre_of_7()

def sum(a,b): 
    return a+b
a = int(input('Enter first num! '))
b = int(input('Enter second num! '))
print(sum(a, b))

def showFullNme(a,b):
    return a+"  "+b
a = 'Mahrokh'
b = 'Ebrahimi'
print(showFullNme(a,b))

print('====================================================================')
dictionary = { 'first_item': 'ghomeSabzi', 'second_item':'shambelile' }
def sabziFunc(a, b):
    return a + '  '+ b
x = sabziFunc(dictionary['first_item'], dictionary['second_item'])
print(x)