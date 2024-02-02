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
#by using .append method:

cel=[0,32,11,23]
far=[]
for temp in cel:
    far.append((9/5)*temp+32)
print(far)

#by using list comphrensation:

faranhite=[((9/5)*temp+32) for temp in cel]
print(faranhite)