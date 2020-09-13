for num in range(1, 10):
    print('*' * num)

print('==================================')


for j in range(10):
    if j%2!=0:
        for m in range(6):
            print('*' * m)
    else:
        for m in range(5, 0, -1):
            print('*' * m)
            
print('==================================')

for i in range(10):
    star = ''
    for j in range(i):
        star = star + '*'
        print(star)

    

