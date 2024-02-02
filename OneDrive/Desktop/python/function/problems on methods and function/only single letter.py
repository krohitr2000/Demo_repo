#-------------------------------------------------------------------------------
# Name:        module4
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
"""Write a Python function that takes a list and returns a new list with unique
 elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]"""
list=[1,1,1,2,2,2,2,3,4,5,5,5,6,6,7,7,8]
def unique(numlist):
    unique_list=[]
    for i in numlist:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
print(unique(list))
