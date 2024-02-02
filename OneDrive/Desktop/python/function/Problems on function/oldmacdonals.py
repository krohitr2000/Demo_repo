#-------------------------------------------------------------------------------
# Name:        module4
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
"""OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald"""

def macdonalad(word):
    wword=word
    return wword[0].capitalize()+wword[1:3]+wword[3].capitalize()+wword[4:]
print(macdonalad('macdonald'))