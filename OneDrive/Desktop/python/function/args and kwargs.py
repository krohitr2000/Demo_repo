#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     18-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
def five_percent(*num):
    return sum(num)*0.5
print(five_percent(5,4))

def add(*args):
    return sum(args)
print(add(1,2))
print(add(4,5,6))

def student_info(*marks,**info):
    for question,data in info.items():
        print(question,data)
    return sum(marks)
print(student_info(10,20,30,name='rohit',stream='electrical',clg='pvpit'))
print(student_info(5,5,5,bike=': splendor',village=': palus'))