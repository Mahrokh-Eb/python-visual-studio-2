# defining set
numbers = {1,2,3,4}
print(numbers)

# we can not repeat numbers in set. if we have repeated items, it removes when we print
# we can not use index to call any item
 
# to check if an Specific item exist:
print(4 in numbers) # True

# to print items
for item in numbers:
    print(item)

# we can convert from set to list or oposite way
print(list(numbers))

# to add a new item
numbers.add(777)
print(numbers) 

# to remove an item from set
numbers.remove(777)
print(numbers)

# to remove use discard since it doesn't give an error if wanted item Doesn’t exist
numbers.discard(784)
print(numbers)

# make a copy
x = numbers.copy()
print(x)

# comparing set and it's copy 
print(numbers == x)
print(numbers is x)

# to remove all items in set
numbers.clear()
print(numbers)
