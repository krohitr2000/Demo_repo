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
# by using noraml append method

mystring='rohit'
mylist=[]
for letter in mystring:
    mylist.append(letter)
print(mylist)

#by using list comphereasation method
mystring2='ravindra'
mylist2=[letter for letter in mystring2]
print(mylist2)

# for numbers
numberlist=[number for number in range(0,10)]
print(numberlist)

#operations over numbers
new_list=[number**2 for number in range(0,10)]
print(new_list)

# use of if in it
even_list=[number for number in range(0,10) if number%2==0]
print(even_list)

#use of if and else
even_list2=[num if num%2==0 else 'odd' for num in range(0,20)]
print(even_list2)