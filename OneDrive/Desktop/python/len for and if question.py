#-------------------------------------------------------------------------------
# Name:        module3
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
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    a=len(word)
    if a%2==0:
        print(word)
    else:
        print('even')