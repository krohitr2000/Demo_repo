#-------------------------------------------------------------------------------
# Name:        module1
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
"""LESSER OF TWO EVENS: Write a function that returns the lesser of two given
numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5"""
def myfunc(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(myfunc(6,2))