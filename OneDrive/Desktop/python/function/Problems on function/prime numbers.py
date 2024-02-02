#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     21-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""def is_prime(numbers):
    primenumbers=0
    for i in range(2,numbers):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag = 1
        if flag==0:
            #print(i)
            primenumbers+=1
    return primenumbers
print(is_prime(30))"""



def is_prime(numbers):
    primenumber=0
    for i in range(2,numbers): # i= 2,3,4,5,6,7,8,9
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
        if flag==0:
            primenumber+=1
    return primenumber
print(is_prime(10))
