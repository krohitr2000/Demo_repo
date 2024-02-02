#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      SCS
#
# Created:     24-07-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
'''Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the number,
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"'''
for i in range(1,100):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
    elif(i%5==0):
        print('Buzz')
    elif(i%3==0):
        print('Fizz')
    else:
        print(i)