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
#map function is used to use list of objects outside the functiobn
def sum(n):
    sum=n+n
    return sum
#here numbers is the list that is uesd outside the function
numbers=(1,2,3,4,5)
result=map(sum,numbers)
print(list(result))


mylist=['rohit','arush','rucha','vidhi']

print(list(map(list,mylist)))