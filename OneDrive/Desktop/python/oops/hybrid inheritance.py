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
class University:
    def __init__(self,name):
        self.name=name
    def show_details(self):
        print(f'name is {self.university}')

class Course(University):
    def __init__(self,name,course_name):
        University.__init__(self,name)
        self.course_name=course_name
        print(f'name of university is {self.name} and course name is {self.course_name}\n')

class Branch(University):
    def __init__(self,name,branch_name):
        University.__init__(self,name)
        self.branch_name=branch_name
        print(f'name of university is {self.name} and branch name is {self.branch_name}\n')

class Student(Course,Branch):
    def __init__(self,course_name,branch_name,my_name,name):
        #University.__init__(self,name)
        Course.__init__(self,course_name,name)
        Branch.__init__(self,branch_name,name)
        self.my_name=my_name
        print(f'my name is {self.my_name} and my course is {self.course_name}, I am studying {self.branch_name}')

class Faculty(Branch):
    def __init__(self,branch_name,fac_name):
        Branch.__init__(self,name,branch_name)
        self.fac_name=fac_name
        print(f'i am faculty my name is {self.fac_name} and i am in {self.branch_name} branch')

course_1=Course('pvpit','electrical')
barnch_1=Branch('tkiset','Cs')
student_1=Student('engineering','mchanical','ajay','pvpit')