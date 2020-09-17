
#doubling numbers, using for 
numbers = [1,2,3,4,5,6] # output: [2, 4, 6, 8, 10, 12]
doubles =[]
for i in numbers:
    doubles.append(i*2)
print(doubles)

# using map()
double2 = map(lambda i : i*2, numbers)
print(list(double2))

# using map() to show char as uppercase
name = ['mah', 'fatai', 'goldane', 'shakazm']
uppernames = map(lambda name: name.upper(), name)
print(name, list(uppernames))

# make a dictionary in a list and return last name
nameFamily = [{'first name ': 'Mona', 'last name': 'goldani'}, 
{'first name ': 'lona', 'last name': 'laghali'}, 
{'first name ': 'moryan', 'last name': 'moyalnizadeh'}]

#using for loop
families2=[]
for i in nameFamily:
    families2.append(i['last name'])
print(families2)

# using map()
families = map(lambda i: i ['last name'], nameFamily)
print(list(families))


