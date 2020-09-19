# built in Functions ,j44
numbers = [2, 6, 7, 18, 90]
print('the maximum of above list is: ',max(numbers)) #  90

names = ['sara', 'mamad', 'golbahar', 'sajadSogholme', 'sharareh', 'zolfaghar']
print(max(names)) #zolfaghar
print(min(names)) #golbahar
 
print('len(names)= ',len(names)) #how many items does the names list have , 6
result = [len(i) for i in names] #it gives the size of char in per name = [4, 5, 8, 13, 8, 9]
print('size of char in per name = ',result)

print(max(names, key= lambda i: len(i))) # the name that has more lenght = sajadSogholme

print(min(names, key= lambda i: len(i))) #sara