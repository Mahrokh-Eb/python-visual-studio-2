# all() Truthiness , Falseness -j43

numbers = [2,4,6,8,7]
# check all numbers to see if they can be devided by 2 
print([num for num in numbers if num%2==0]) # [2, 4, 6, 8]

print([num%2==0 for num in numbers]) # [True, True, True, True, False]

print(all([num%2==0 for num in numbers])) # False 

# any() if only one item=True, it returns true
numbers2 = [0,0,0,0]
print(any(numbers2)) # False
