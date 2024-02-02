#-------------------------------------------------------------------------------
# Name:        module7
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
"""Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False"""

def has_33(arr):
    for i in range(0,len(arr)):
        if arr[i]==3 and arr[i+1]==3:
            return True
    return False
print(has_33([1,2,3,8,3,3]))