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
    def __init__(self,num_heart):
        self.num=num_heart
        self.eyes=2
    def eat(self):
        print('i can eat')

    def work(self):
        print('i can work')
class Male(Human):
    def __init__(self,num_heart,can_dance):
        self.dance=can_dance
    def sleep(self):
        print('i can sleep')
class Boy(Male):
    def work(self):
        #Male.work(self)
        super().work()
        print('i can not work')
class Worker(Boy):

    def work(self):
        self.eyes=3
        print('i can do all work')
boy_1=Boy('not',True)
#boy_1.eat()
#boy_1.sleep()
#boy_1.work()
worker_1=Worker('present',True)
#worker_1.work()
print(boy_1.num)
print(worker_1.num)
print(boy_1.eyes)
print(worker_1.eyes)