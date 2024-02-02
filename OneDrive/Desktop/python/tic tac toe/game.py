#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      SCS
#
# Created:     05-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from random import randint
def game_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
"""empty_board=['#','X','X','X','','','','','','']
game_board(empty_board)"""

def user_input():
    marker=''
    while not(marker=='X' or marker=='O'):
        marker=input('player 1 please enter your choice X or O').upper()
    if marker=='X':
        return ('x','O')
    else:
        return ('O','X')
#print(user_input())

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
#print(win_check(empty_board,'X'))


def first_chance():
    flip= randint(0,1)
    if flip==0:
        return 'player 1 '
    else:
        return 'player 2 '
#print(first_chance())

def space_check(board,position):
    return board[position]==''
#print(space_check(empty_board,9))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def position_check(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('enter your position : (from 1 to 9)'))
    return position

def replay():
    choice=input('Play again ? (Y or N)')
    return choice=='Y'


print('Welcome !')
while True:

    the_board=[ ]*10
    player1_marker,player2_marker=user_input()

    turn = first_chance()
    print(turn+' will go first')

    play_game= input('ready ? (y or n)')
    game_on=True
    if play_game=='y':
        game_on= True
    else:
        game_on= False

    while game_on==True:
        if turn=='player 1':
            game_board(the_board)

            position=position_check(the_board)

            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                game_board(the_board)
                print('player 1 has won !')
                game_on=False
            else:
                if full_board_check(the_board):
                    game_board(the_board)
                    print('Its a tie !')
                    game_on=False
                else:
                    turn='player 2'

        else:
            game_board(the_board)

            position=position_check(the_board)

            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                game_board(the_board)
                print('player 2 has won !')
                game_on=False
            else:
                if full_board_check(the_board):
                    game_board(the_board)
                    print('Its a tie !')
                    game_on=False
                else:
                    turn='player 1'


    if not replay():
        break