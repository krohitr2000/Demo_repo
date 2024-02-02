#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     09-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class instructor:
    pass
instructor1=instructor()
print(type(instructor1))

#self and init method:

class instructor:
    def __init__(self):
        print('this is instance!\n')
        print('this line will be printed when object is created !\n')
instructor1=instructor()
instructor()
instructor2=instructor()

