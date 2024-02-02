#-------------------------------------------------------------------------------
# Name:        module5
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
count=0
while(n>0):
    count=count+1
    n=n//10
print(count)