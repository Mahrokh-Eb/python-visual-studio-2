# handle the errors via try and except

try:
    print(hi)
except:
    print('Hello Printing dictionary, using function')


#defining a function
def get(d, key): 
    return d[key]

# defining a dictionary
person = {
    'name': 'Mahrokh',
    'lastname': 'Ebrahimi', 
    'age': '34'
}
print(person['name'], person['lastname']) # mahrokh Ebrahimi
print(get(person, 'name')) # mahrokh