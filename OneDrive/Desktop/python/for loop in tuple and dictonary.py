#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      SCS
#
# Created:     14-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#for loop im tuple
x=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in x:
    print (b,c)

#for loop im dictonary
x={'k1':1,'k2':2,'k3':3,'k4':4}
for values,keys in x.items():
    print(values)