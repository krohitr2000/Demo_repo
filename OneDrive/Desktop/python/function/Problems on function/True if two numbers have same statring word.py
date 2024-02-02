#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      SCS
#
# Created:     19-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""ANIMAL CRACKERS: Write a function takes a two-word string and returns
True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False"""

def myfunc(text):
    new_text=text.split()
    return new_text[0][0]==new_text[1][0]
print(myfunc('ohit opaja'))