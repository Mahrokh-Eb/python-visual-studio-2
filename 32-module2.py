# making colors
import termcolor
# print(termcolor.colored('Python in color', color = 'red'))
# print(termcolor.colored('Python in color', color = 'green'))
# print(termcolor.colored('Python in color', color = 'yellow'))
# print(termcolor.colored('Python in color', color = 'blue'))
# print(termcolor.colored('Python in color', color = 'cyan'))

# python-visual-studio-2 mahrokh$  python -m pip install pyfiglet
import pyfiglet
from termcolor import colored 
# print(pyfiglet.figlet_format('Python'))

# message = input('What would you like to print? ')
# color = input('what color? ')
# acii_art = pyfiglet.figlet_format(message)
# acii_art = colored(acii_art, color)
# print(acii_art)


# using function to write 
valid_colors = ['red', 'yellow', 'cyan', 'green', 'blue']
def pyfigletColor(message, color):
    if color not in valid_colors:
        color = 'red'
    acii_art = pyfiglet.figlet_format(message)
    acii_art = colored(acii_art, color)
    print(acii_art)

message = input('What would you like to print? ')
color = input('what color? ')
pyfigletColor(message, color)



