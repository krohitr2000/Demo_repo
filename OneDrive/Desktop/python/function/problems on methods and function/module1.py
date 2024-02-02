#-------------------------------------------------------------------------------
# Name:        module1
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
#Write a function that checks whether a number is in a given range (inclusive of high and low)

def check(num,low,high):
    return num>low and num<high
print(check(9,2,7))