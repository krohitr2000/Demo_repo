#-------------------------------------------------------------------------------
# Name:        module2
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
"""Write a Python function that accepts a string and calculates the number of
upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33"""

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    uppers=0
    lowers=0
    for i in s:
        if i.isupper():
            uppers+=1
        elif i.islower():
            lowers+=1
        else:
            pass
    return uppers,lowers
print(up_low(s))