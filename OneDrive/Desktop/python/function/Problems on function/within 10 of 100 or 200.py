#-------------------------------------------------------------------------------
# Name:        module6
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
"""ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True"""

def within_ten(n):
    return abs(100-n)<=10 or abs(200-n)<=10
print(within_ten(180))