#-------------------------------------------------------------------------------
# Name:        module11
# Purpose:
#
# Author:      SCS
#
# Created:     19-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""SPY GAME: Write a function that takes in a list of integers and returns
True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False"""

def spy_game(numbers):
    numlist=[]
    for num in(numbers):
        numlist.append(num)
    for i in range(len(numlist)):
        if numlist[i]==0 and numlist[i+1]==0 and numlist[i+2]==7:
            print('correct')
    return numlist
print(spy_game([1,0,2,4,0,5,7]))

"""def spy_game(nums):

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

    return len(code) == 1"""

def spygame(numbers):
    code=[0,0,7,'x']
    for i in numbers:
        if i==code[0]:
            code.pop(0)
    return len(code)==1
print(spygame([1,0,2,4,0,5,7]))
