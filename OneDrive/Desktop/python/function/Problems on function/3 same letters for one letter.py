#-------------------------------------------------------------------------------
# Name:        module8
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
"""PAPER DOLL: Given a string, return a string where for every character in the
 original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'"""

def paper_doll(name):
    for i in (name):
        result=i*3
    return result
print(paper_doll('rohit'))