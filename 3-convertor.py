'''programmer: Mahrokh Ebrahimi
Description: user enter a number as a km. it will convert to mile
Date: 9/9/2020'''

km = float(input('Enter a kilometer to convert it to mile: ') )

mile = km / 1.6
mile = round(mile, 2)

print(f'kilometer is {km} and it is going to be {mile} miles')
print('Dpne!')
