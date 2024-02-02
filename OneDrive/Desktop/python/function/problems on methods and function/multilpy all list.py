#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      SCS
#
# Created:     02-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""Write a Python function to multiply all the numbers in a list."""
nlist=[1,2,3,4,]
def multi(numlist):
    total=1
    for i in (numlist):
        total*=i
    return total
print(multi(nlist))