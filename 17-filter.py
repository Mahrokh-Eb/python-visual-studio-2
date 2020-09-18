numbers = [1,2,3,4,5,6,7,8]
evens = filter(lambda num: num%2==0, numbers)
print(list(evens))

users = [{'name': 'fati', 'Shopping card':[]}, 
{'name': 'safoora', 'Shopping card':['kotlin', 'python']},
{'name': 'sogholme', 'Shopping card':[]}
]
print(len(users))  # 3
result = filter(lambda i: len(i['Shopping card'])==0, users)  
print(list(result)) # [{'name': 'fati', 'Shopping card': []}, {'name': 'sogholme', 'Shopping card': []}]

# first give all user's name
result1 = map(lambda i: i['name'], users)  
print(list(result1)) # ['fati', 'safoora', 'sogholme']

# combining filter() & map
# it gives the users who their Shopping card is empty 
result2 = map(lambda i: i['name'], filter(lambda i: len(i['Shopping card'])==0, users))  
print(list(result2))  # ['fati', 'sogholme']

# it gives the users who their Shopping card is empty with for instead of map() & filter()
result3 = [i['name'] for i in users if len(i['Shopping card'])==0]
print(result3) #['fati', 'sogholme']