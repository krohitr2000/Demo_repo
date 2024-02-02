#-------------------------------------------------------------------------------
# Name:        module2
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
""" Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples
of both three and five print "FizzBuzz"."""

for num in range(1,100):
    if(num%3==0) and (num%5==0):
        print('FizBuzz')
    elif(num%3==0):
        print('Fizz')
    elif(num%5==0):
        print('Buzz')
    else:
        print(num)