#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-07-13
Purpose: REturning the maximum of any three numbers as user input
"""

def maxNum():

    x= float(input("Enter first number: "))
    y= float(input("Enter second number: "))
    z= float(input("Enter third number: "))

    if (x >=y) and (x >=z):
        max_num = x
    elif (y >=x) and (y >=z):
        max_num = y
    else:
        max_num = z

    print('The maximum number is', max_num)


maxNum()

