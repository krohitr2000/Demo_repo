#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     11-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class Animal:
    def __init__(self):
        print('class is created\n')
    def eat(self):
        print('i like to eat\n')
    def sound(self):
        print('i have my sound\n')
animal=Animal()
animal.sound()
animal.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        #print('class dog is created')
mydog=Dog()
mydog.sound()