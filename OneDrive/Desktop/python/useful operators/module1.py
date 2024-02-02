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
word=input('enter any word : ')
index_count=1
for letter in word:
    print(index_count)
    index_count+=1

#by using enumarate function
new_word='abcdef'
for number,letter in enumerate(new_word):
    print(letter)