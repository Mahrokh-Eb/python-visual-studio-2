# how to get copy from list items
# list sclicinig
myNumbers = [1,2,3,4,5,6,7,8,9]

#gives one integer
selectedNum = myNumbers[2]
print(selectedNum)

# some_list[start:end:step] , gives a list
selectedNumfromList = myNumbers[2:7:1]
print(selectedNumfromList)

# copy from all of items
copyAllitem = myNumbers[:]
print(f'copy of all items: {copyAllitem}')

# reverse of list
color = ['red', 'green', 'pink', 'black'] 
color.reverse()
print(color)