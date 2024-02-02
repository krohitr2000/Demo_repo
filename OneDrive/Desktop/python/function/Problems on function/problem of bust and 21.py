#-------------------------------------------------------------------------------
# Name:        module9
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
"""BLACKJACK: Given three integers between 1 and 11, if their sum is less than
or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds
21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19"""

def blackjack(a,b,c):
    sum=a+b+c
    if sum<=21:
        return sum
    elif sum>21 and 11 in(a,b,c):
        return (sum-10)
    else:
        return 'Bust'
print(blackjack(9,9,11))
