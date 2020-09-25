# difining defferent errors:

# making different errors by ourselfes
# raise IndexError('it is index error')


def colorize (text, color):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError('text must be string')
    elif color not in colors:
        raise ValueError(f'{color} should be in {colors} tuple')
    else:
        print(f'printed {text} in {color}')

colorize('hello', 'pink') # if i put pink, ValueError: pink should be in ('red', 'green', 'blue') tuple
colorize('hello', 'red') # printed hello in red 
colorize( 2 , 'red') # TypeError: text must be string