#-------------------------------------------------------------------------------
# Name:        module2
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
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.follower=0
        self.following=0

    def display(self,subject_name):
        print(f'Hi i am {self.name} and i teach {subject_name} ')

    def update_follower(self,name):
        self.follower=1

    def update_following(self,number):
        self.following=2
instructor1=instructor('rohit','palus ')
print(instructor1.name,instructor1.address)
instructor1.display('english')
instructor1.update_follower('raj')
print(instructor1.follower)
instructor1.update_following(12)
print(instructor1.following)