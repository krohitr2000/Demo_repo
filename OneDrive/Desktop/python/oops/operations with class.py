#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      SCS
#
# Created:     09-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class circle:
    pi=3.147
    def __init__(self,radius):
        self.radius=radius
    def Circumference(self):
        return 2*self.pi*self.radius
Circle1=Circle(4)
print(Circle1.Circumference())

class Area:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
rectangle=Area(6,3)
print(rectangle.area())

class Sums:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def sum(self):
        return self.num1+self.num2
addition=Sums(10,10)
print(addition.sum())