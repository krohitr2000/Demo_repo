#-------------------------------------------------------------------------------
# Name:        module2
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
result=shuffle_list(example)
print(result)
mylist=['','0','']
result= shuffle_list(mylist)
print(result)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('guess number between 0, 1 or 2 :')
    return int (guess)
player_guess()

def check_guess(mylist,guess):
    if mylist[guess]==0:
        print('Correct!')
    else:
        print('wrong')
        print(mylist)

mylist=['','0','']

mixedup_list=shuffle_list(mylist)

guess=player_guess()

check_guess(mixedup_list,guess)

