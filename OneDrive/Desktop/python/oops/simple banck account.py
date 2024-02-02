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
class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
        print(f'{self.amount} amount is added')
    def withdrawal(self,with_amount):
        self.with_amount=with_amount
        if self.balance>=with_amount:
            self.balance-=with_amount
            print(f'{self.with_amount} amount is withdrwaen')
        else:
            print('insufficient funds !')
    def __str__(self):
        return f'owner : {self.owner}\nbalance : {self.balance}'
account_1=Account(input('enter your name :'))
account_1.deposit(int(input('enter amount to be added : ')))
account_1.withdrawal(int(input('enter amount to withdrwa : ')))
print(account_1)
