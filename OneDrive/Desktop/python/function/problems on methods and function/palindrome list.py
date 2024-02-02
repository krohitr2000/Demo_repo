#-------------------------------------------------------------------------------
# Name:        module6
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
"""Write a Python function that checks whether a word or phrase is palindrome or not."""
s='nurses run'
def palindrome(sentence):
    sentence=sentence.replace(' ','')
    return sentence==sentence[::-1]
print(palindrome(s))