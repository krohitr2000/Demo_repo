#-------------------------------------------------------------------------------
# Name:        module4
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
def even_check_list(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass
    return False
new_list=even_check_list([11,221,33,458])
print(new_list)