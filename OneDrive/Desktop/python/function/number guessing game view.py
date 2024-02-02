#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     27-07-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
example=[1,2,3,4,5]
from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

newlist=['','0','']
result=shuffle_list(newlist)
print(result)

def user_guess():
    guess=''
    while guess not in['0','1','2']:
        guess=input('choose number :')
    return int(guess)
user_guess()

def check_guess(newlist,guess):
    if newlist[guess]=='0':
        print('Correct!')
    else:
        print('Wrong')
        print(newlist)

game_list=['','0','']

new_shuffeled_list=shuffle_list(game_list)

player_guess=user_guess()

result=check_guess(new_shuffeled_list,player_guess)