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
def sabziFunc(a, b): # parameters
    return f'{a} {b}' 
x = sabziFunc(dictionary['first_item'], dictionary['second_item']) # calling the func- argoman
print(x)

print('====================================================================')
def sum_odd_numbers(numbers):
    sum = 0
    for i in numbers:
        if i%2 != 0:
            sum = sum + i
    return sum

numbers = [1,2,3,4,5,6,7] 
print(f'the sum of odd numbers is: {sum_odd_numbers(numbers)}')