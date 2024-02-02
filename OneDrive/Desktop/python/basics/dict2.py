#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      SCS
#
# Created:     11-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
d={'k1':23,'k2':[1,2,3],'k3':'rohit'}
mylist=d['k2']
print(mylist)
print(mylist[2])
print(d['k2'][2])

e={'r1':'rohit','r2':'rucha','r3':'ravindra'}
print(e['r2'][2:].upper())
e['r4']='rajani'
print(e)
e['r1']=300
print(e['r1'])

print(e.values())
print(e.keys())
print(e.items())