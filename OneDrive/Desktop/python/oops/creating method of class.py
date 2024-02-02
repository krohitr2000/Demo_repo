#-------------------------------------------------------------------------------
# Name:        module1
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
class instructor:
    def __init__(self,name,age,address):
        self.instname=name
        self.instage=age
        self.instadress=address
        #default value:
        self.floowers=0

instructor1=instructor('rohit',22,'palus'+'raj')
instructor2=instructor('ro',222,'palus')
instructor3=instructor('hit',322,'palussangli')
print(instructor1.instname,instructor1.instage,instructor1.instadress)
print(instructor2.instname,instructor1.instage,instructor3.instadress,instructor3.floowers+123345)

print(instructor1.floowers)
print(instructor2.floowers)