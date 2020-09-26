# handle the errors via try and except

try:
    print(hi)
except:
    print('Hello Printing dictionary, using function')


#defining a function
def get(d, key): 
    try:
        return d[key]
    except KeyError:
        return('nemigam, Not Available!')
    except IndexError:
        return('index probem')


# defining a dictionary
person = {
    'name': 'Mahrokh',
    'lastname': 'Ebrahimi', 
    'age': '34'
}
print(person['name'], person['lastname']) # mahrokh Ebrahimi
print(get(person, 'gol')) # mahrokh


# check if user enter int or str
try:
    num = int(input('Enter a number: '))
except:
    print('that is not a number! ')

# while and try, except, else, finally
while True:
    try:
        num = int(input('Enter an integer for trying try, except, else, finally:  '))
    except:
        print('that is Not an integer')
    else:
        print('bravo! that is a number.')
        break
    finally:
        print('it shows anyway. ')