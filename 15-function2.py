# making parameter of the function Dinamically 
def parameterDynamic(name, *arg):
    print(name)
    total = 0
    for i in arg:
        total += i
    return total
print(parameterDynamic('sum of the numbers: ',1, 1, 1, 1, 1, 1)) # sum of the numbers: 6

print('====================================================================================')
#  printing like a dictionary
def dictionary(**kwargs):
    for i, j in kwargs.items():
        print(i,':',j)
dictionary(name='Mahi', lastname='Ebrahimi', DOB='September', age= 33, email='mebrahimi@ucla.edu')

print('====================================================================================')
# the order of the parameters fo the function
def orderdef(a, b, *args, c = 'defaullf', **kwargs ):
    return[a, b, args, kwargs]
print(orderdef(1, 2, 3, 4, m='fafarimerriri' ))
