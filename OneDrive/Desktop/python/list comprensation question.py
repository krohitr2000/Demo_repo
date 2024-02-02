#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      SCS
#
# Created:     24-07-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist=[x for x in range (1,50) if x%3==0]
print(mylist)