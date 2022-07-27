#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-07-23
Purpose: Creating a bank account 
"""

# Class


class Bank_Account:
    # class level attribute
    Balance = 500000
# The Init method

    def __init__(self, name=str, Acc_number=int, user_address=str, phone_number=int,
                 account_type=str, age=int, created_at=str, updated_at=str, state_of_origin=str,):
        self.name = name
        self.Acc_number = Acc_number
        self.user_address = user_address
        self.phone_number = phone_number
        self. account_type = account_type
        self.age = age
        self.created_at = created_at
        self.updated_at = updated_at
        self.state_of_origin = state_of_origin
        self.email = self.name + "@gmail.com"
# The deposit method

    def deposit(self):
        amount = float(input('Enter the amount to be deposited: '))
        Bank_Account.Balance = Bank_Account.Balance + amount
        print("Transaction sucessful! Your account balance is:")
# The withdrawal method

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (Bank_Account.Balance > amount):
            Bank_Account.Balance = Bank_Account.Balance - amount
            print("Transaction sucessfull! Your account balance is:")
        else:
            print("Insuficient Balance")


# Instantiation
Account = Bank_Account('Victoria', 4356366635, 'Surulere, Lagos State Nigeria',
                       '08100000000', 'savings account', 35, '15-05-2019', '23-07-2022', 'Kwara state',)


Account.deposit()
print(Account.Balance)

Account.withdraw()
print(Account.Balance)
