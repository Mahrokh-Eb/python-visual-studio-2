# importing modules:

#import random
#import random as rand
from random import randint, choice
# from random import *

print(randint(1, 100)) # gives a number beetween 1, 100
myCourses = ['Python', 'xml', 'jquery', 'java', 'kotlin'] 
print(choice(myCourses )) # select one of the above list

# mdule for circle and Rectangular is made by myself
import circle
print('The area of circle for r=2 is: ',circle.AreaCircle(2))

import rectangular
print('The area of Rectangular for h=4, w=6 is: ', rectangular.rectangularArea (4,6))
