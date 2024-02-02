#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     11-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
my_list=[1,2,3,4]
print(my_list[3])
another_list=[9,8,7,6]
another_list[2]='seven'
print(another_list)
print(my_list+another_list)
my_list.append(10)
my_list.append(20)
print(my_list)
my_list.pop()
print(my_list)
poped_item=my_list.pop()
print(poped_item)

n_list=['r','u','c','h','a']
num_list=[7,4,1,5,9,2]
num_list.sort()
print(num_list)
n_list.sort()
print(n_list)
num_list.reverse()
print(num_list)