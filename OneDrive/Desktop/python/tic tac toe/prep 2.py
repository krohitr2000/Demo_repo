#-------------------------------------------------------------------------------
# Name:        module2
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
game_list=[0,1,2]
def user_choice(game_list):
    print('the current list is :')
    print(game_list)
#user_choice(game_list)

def display_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice=input('enter choice between 0,1,2 :')
        if choice not in ['0','1','2']:
            print('invalid choice !')
    return int(choice)
#display_choice()

#user_position=int(input('enter position : '))
def replacement(game_list,position):
    user_choosen=input('enter string to enter at position :')
    game_list[position]=user_choosen
    return game_list
#print(replacement(game_list,user_position))

def game_on():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input('continue game ? , (Y or N)')
        if choice not in ['Y','N']:
            print('invalid choice please enter Y or N')
    if choice == 'Y':
        return True
    else:
        return False
    return choice
#game_on()

gameon_choice=True
game_list=['0','1','2']
while gameon_choice:
    user_choice(game_list)
    display_choice()
    user_position=int(input('enter position : '))
    game_list=replacement(game_list,user_position)
    gameon_choice=game_on()