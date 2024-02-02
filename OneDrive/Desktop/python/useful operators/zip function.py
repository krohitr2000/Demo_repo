#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     16-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
list1=[1,2,3,4,5,6]
list2=['a','b','c','d']
list3=['rohit','raj','vidhi']

zip(list1,list2,list3)
print(zip(list1,list2,list3))

for item in zip(list1,list2,list3):
    print(item)

#to print zip file as list:

print(list(zip(list1,list2,list3)))