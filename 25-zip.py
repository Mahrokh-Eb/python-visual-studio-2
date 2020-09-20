numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]
 
result = zip(numbers_1, numbers_2)
print(list(result)) #[(1, 5), (2, 6), (3, 7), (4, 8)]
print(dict(result)) #{1: 5, 2: 6, 3: 7, 4: 8}

mylist = [(1, 5), (2, 6), (3, 7), (4, 8)]
print(list(zip(*mylist)))  # [(1, 2, 3, 4), (5, 6, 7, 8)]

# example:
students = ['ali', 'sara', 'kachi']
midterm = [99, 88, 55]
final = [77, 55, 88]
