# nested list

numbers = [[1,2,3], [4,5,6]]
print(numbers[1][2])

for i in numbers:
    print(i)

print('=================================')

for i in numbers:
    for j in i:
        print(j)