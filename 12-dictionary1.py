myNumbers = [1,2,3,4,5,6]
names = ['sara', 'sahar', 'sajad']

# dictionary = {key: 'value'}

dictionary1 = {'item':'golbahar', 'price': '234', 'count':'8'}
print(dictionary1)

# to call an item
print(dictionary1['item'])

# to creat dict, way2
dictionary2 = dict(name='goldane', price='98', count='88')
print(dictionary2)

print(dictionary2['name'])

print('========================================================')
# make a new dictionary
me={
    'name': 'Mahi jan', 
    'family': 'goldanekhani', 
    'age': '30 o andi', 
    'property' : 'Hardworking'
}

print(me.values())
print(me.keys())
 
#print(me['name'])
for i in me.values():
    print(i)