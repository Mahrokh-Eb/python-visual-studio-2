# sorting items
numbers = [1, 9, 3, 4, 7, 2, 8]
numbers.sort()
print(numbers) #[1, 2, 3, 4, 7, 8, 9]

result2 = sorted(numbers)
print(result2) 
print(numbers) # it shows previous number list again

# sorting the dictionary
users = [{'name': 'kobra'}, {'name': 'fati'}, {'name': 'gholi'}, {'name': 'golmamad'}, {'name': 'ozra'}]
print(sorted(users, key= lambda i : i['name'])) 
# output: [{'name': 'fati'}, {'name': 'gholi'}, {'name': 'golmamad'}, {'name': 'kobra'}, {'name': 'ozra'}]