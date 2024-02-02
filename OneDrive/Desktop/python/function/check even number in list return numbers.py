#-------------------------------------------------------------------------------
# Name:        module6
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
def check_even_list(num_list):
    even_number=[]
    for number in num_list:
        if number%2==0:
            even_number.append(number)
        else :
            pass
    return even_number
new_list = check_even_list([22,23,445,78,98,88])
print(new_list)