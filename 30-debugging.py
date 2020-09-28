# pythom debugger
import pdb
pdb.set_trace( )

number1 = int(input('Ebter num-1: '))
number2 = int(input('Ebter num-2: '))
total = number1 + number2
print(f'number1 plus number2 = {total}') 

# debugging commands , put in Terminal
# l -> your command list
# n -> next line
# c -> Continue 
# p -> print


# l: (Pdb) l output for Entering l in terminial
'''  1     # pythom debugger
  2     import pdb
  3     pdb.set_trace( )
  4  
  5  -> number1 = int(input('Ebter num-1: '))
  6     number2 = int(input('Ebter num-2: '))
  7     total = number1 + number2
  8     print(f'the sume of number1 and number2= {total}')'''

