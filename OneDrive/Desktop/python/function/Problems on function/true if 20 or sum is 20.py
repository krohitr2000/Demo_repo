#-------------------------------------------------------------------------------
# Name:        module3
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
"""MAKES TWENTY: Given two integers, return True if the sum of the integers is
20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False"""

def make_twenty(a,b):
    return a==20 or b==20 or a+b==20
print(make_twenty(18,2))