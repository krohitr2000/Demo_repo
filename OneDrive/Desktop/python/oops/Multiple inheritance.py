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
class Human:
    def __init__(self,name):
        self.name=name
        print('in it from human')
#human=Human('rohit')
#print(human.name)

class Male:
    def __init__(self,name):
        self.name=name
        print('This is from male')
    def sum(self,num):
        self.num=num
        num=2+2
        return num

class Boy(Human,Male):
    def __init__(self,name):
        super().__init__(Human)
        Male.__init__(self,name)
        print('in it from boy')
    def display(self):
        print(f'hi i am {self.name} and sum is {self.num}')
boy=Boy('rucha')
print(boy.name)

Male.display(boy)