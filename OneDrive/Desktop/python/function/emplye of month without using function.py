#-------------------------------------------------------------------------------
# Name:        module7
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
workimg_hrs=[('rohit',1992),('raj',1162),('jay',374)]
new_hrs=0
employe=''
for name,hrs in workimg_hrs:
    if hrs>new_hrs:
        new_hrs=hrs
        employe=name
print(employe,new_hrs)

        #print(employe,new_hrs)