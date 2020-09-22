numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]
 
result = zip(numbers_1, numbers_2)
print(list(result)) #[(1, 5), (2, 6), (3, 7), (4, 8)]
print(dict(result)) #{1: 5, 2: 6, 3: 7, 4: 8}

mylist = [(1, 5), (2, 6), (3, 7), (4, 8)]
print(list(zip(*mylist)))  # [(1, 2, 3, 4), (5, 6, 7, 8)]

# example:
students = ['ali', 'sara', 'kachi']
midterm = [99, 78, 55]
final = [77, 55, 89]

# I want a dictionary to be returned with per name and the max number
finalGrade_1 = [pair for pair in zip(midterm, final)]
print(finalGrade_1) #[(99, 77), (78, 55), (55, 89)]

finalGrade_2 = [max(pair) for pair in zip(midterm, final)]
print(finalGrade_2)  #[99, 78, 89]

final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterm, final)}
print(final_grades) #{'ali': 99, 'sara': 78, 'kachi': 89}

