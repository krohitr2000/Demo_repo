#-------------------------------------------------------------------------------
# Name:        module2
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
    def __init__(self):
        self.nose=1
        self.eyes=2
    def name(self):
        print('my name is rohit')
    def work(self):
        print(' I can work')
    def play(self):
            print('I can play')
class Male(Human):
    #   method(function) in inheritance can be overridden
    def name(self):
        print(' my name is raj')

#   if you define any other methdo in child class it will show error for derived methods from parent class:

    # so you have to use super() function:
    def __init__(self,education):
        super().__init__() #    super function do not have : sign in it
        self.edu=education

#   method can be overridden by using already existing method
class Female(Human):
    def name(self):
        super().name()
        print('my name is rucha')
    def __init__(self,village):
        super().__init__()
        self.vil=village

male1=Male('graduate')
male1.name()
human1=Human()
human1.name()
female1=Female('palus')
female1.name()
#   attributes from parent class can be accessed by child class:
print('male have', male1.eyes, 'eyes')
print('female has ',female1.nose,'nose')

# you can now call it :
print(male1.edu)

print(female1.vil)

