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
def sqr(num):
    return num*num
mynum=[1,2,3,4,5,6,7,8,9]
result=map(sqr,mynum)
print(list(result))

def prime(n):
    return n*2==16
newnum=[1,2,3,4,5,6,7,8,9]
res=filter(prime,newnum)
print(list(res))

square=lambda num:num*num
print(square(5))
print(square(9))

mynums=[1,2,3,4,5,6,7,8]
#lamnda in map function
print(list(map(lambda n:n*5,mynums)))
print(list(map(lambda n:n*n,mynums)))

#lambda in filter function
print(list(filter(lambda n:n%2==0,mynums)))
print(list(filter(lambda n:n*2==16,mynums)))


names=['rohit','rucha','vinita','ravikaka']
print(list(map(lambda name:name[1],names)))
print(list(map(lambda name:name[::-1],names)`````````````````))