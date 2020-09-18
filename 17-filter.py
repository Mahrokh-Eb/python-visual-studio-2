numbers = [1,2,3,4,5,6,7,8]
evens = filter(lambda num: num%2==0, numbers)
print(list(evens))

users = [{'name': 'fati', 'Shopping card':[]}, 
{'name': 'safoora', 'Shopping card':['kotlin', 'python']},
{'name': 'sogholme', 'Shopping card':[]}
]
print(len(users))
result = filter(lambda i: len(i['Shopping card'])==0, users)
print(list(result))

# combining filter() & map
# first give all user's name
result1 = map(lambda i: i['name'], users)  
print(list(result1))    

# it gives the users who their Shopping card is empty 
result2 = map(lambda i: i['name'], filter(lambda i: len(i['Shopping card'])==0, users))  
print(list(result2))  

# it gives the users who their Shopping card is empty with for
result3 = [i['name'] for i in users if len(i['Shopping card'])==0]
print(result3)