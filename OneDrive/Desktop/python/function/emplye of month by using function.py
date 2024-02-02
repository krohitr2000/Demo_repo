#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     25-07-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
working_hrs=[('rohit',12),('rajaram',798),('rucha',98)]
def best_employe(working_hrs):
    new_hrs=0
    employe_of_month=''
    for name,hrs in working_hrs:
        if hrs>new_hrs:
            new_hrs=hrs
            employe_of_month=name
        else:
            pass
    return (employe_of_month,new_hrs)
result=best_employe(working_hrs)
print(result)