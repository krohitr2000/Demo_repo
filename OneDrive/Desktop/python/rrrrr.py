#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      SCS
#
# Created:     20-10-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import re
print('***** Welcome *****')
class Account:

    data=[ ]
    password_data=[ ]

    def __init__(self,name='',password='',email=''):
        self.name=name
        self.password=password
        self.email=email

    def username(self,username):
        self.name=username
        print(f'You entered : {username}')
        self.data.append(self.name)

    def is_pass_valid(self,password):
        return(
            len(password) >8 and
            len(re.findall(r'[a-zA-Z])',password)) and
            len(re.finadall(r'[\d])',password))and
            len(re.finadall(r'[!@#$%^&*()_+)',password))
        )
    def userpass(self,user_password):
        self.password= user_password
        if self.is_pass_valid(user_password):
            print('password set successfully')
        else:
            print('Invalid password!')
            print('Password must have 8letters, 4 alphabtes, symbol and number')
            print(f'you entered :{user_password}')
            self.password_data.append(self.password)

        """def userpass(self, user_password):
        self.password = user_password
        if self.is_pass_valid(user_password):
            print('Password set successfully')
        else:
            print('Invalid password!')"""

Account1=Account()
Account1.username(input('enter your name : '))
Account1.userpass(input('enter password : '))
print(Account.data)
