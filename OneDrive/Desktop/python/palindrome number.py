#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      SCS
#
# Created:     21-07-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n=int(input())
temp=n
rev=0
while(n>0):
    #rem=n%10
    rev=rev*10+(n%10)
    n=n//10
print(rev)