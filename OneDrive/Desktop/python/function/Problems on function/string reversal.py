#-------------------------------------------------------------------------------
# Name:        module5
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
"""MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'"""

def words_reverse(sentence):
    new_word=sentence.split()
    return new_word[::-1]
print(words_reverse('hi i am rohit'))