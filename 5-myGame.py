print('Rock')
print('paper')
print('sisears')

player_1 = input('make your move! ')
player_2 = input('make your move! ')

if player_1 == 'Rock' and player_2 =='sisears':
    print('player_1 win!')

elif player_1 == 'Rock' and player_2 =='paper':
    print('player_2 win! ')

elif player_1 == player_2:
    print('you are stocked!')

else:
    print('sth went wrong! ')