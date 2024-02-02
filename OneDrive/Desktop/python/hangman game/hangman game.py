#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     08-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from random import choice
lives=6
word_list=['apple','banana','mango','chips','chiku','vidhi','arush']
chosen_word=choice(word_list)
print(chosen_word)
display=[]
for i in chosen_word:
    display+='-'
print(display)
while lives>0:
    guessed_letter=input('enter your word :').lower()
    for position in range(len(chosen_word)):
        #letter=chosen_word[position]
        if chosen_word[position] == guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives-=1
        print('letter is not in word.')
    if lives==0:
        print('Out of lives, you lose !')
    if '-' not in display:
        print('Congrats ! you won.')
        break
