# nested list

numbers = [[1,2,3], [4,5,6]]
print(numbers[1][2]) # 6 

for i in numbers:
    print(i)

print('=================================')
for i in numbers:
    for j in i:
        print(j)

print('=================================')
copylist = [i for i in numbers ] 
print(copylist)
#[[1, 2, 3], [4, 5, 6]]

print('=================================')
copylist2 = [[print(j) for j in i]for i in numbers]
# print(copylist2)
# 1 2 3 4 5 6 in colum 

print('=================================')
generatedList = [[i] for i in range(1,4)]
print(generatedList)
# [[1], [2], [3]]

print('=================================')
generatedList2 = [[i for i in range(1,4) ]for i in range(1,4)]
print(generatedList2)
#[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print('=================================')
generatedList2 = [['X' if j%2==0 else 'O' for j in range(1,4) ]for i in range(1,4)]
print(generatedList2)

