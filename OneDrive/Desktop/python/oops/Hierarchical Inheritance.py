#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     12-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class Human:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print('I can eat')
class Male(Human):
    def __init__(self,name,age):
        print('in it from male')
        Human.__init__(self,name)
        self.age=age
        print(f'my name is {self.name} and age is {self.age}')
    def sleep(self):
        print('I can sleep')
class Female(Human):
    def work(self):
        print('I can work')

male_1=Male('rohit',22)
male_1.eat()
male_1.sleep()
female1=Female('rucha')
female1.eat()