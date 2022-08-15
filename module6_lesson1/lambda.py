#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-08-09
Purpose: working with lambda in python
"""
# Create a list of integers between 5.5 and 20.5. Write a python program using the lambda function that does the following;

list_1 = [6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# count  the even and odd  numbers in the list .

Even_num = list(filter(lambda x: (x % 2 == 0), list_1))
print(Even_num)

odd_number = list(filter(lambda x: (x % 2 != 0), list_1))
print(odd_number)

# Square and cube every number in the list.

squared = list(map(lambda x: pow(x, 2), list_1))
print(squared)

cubed = list(map(lambda x: pow(x, 3), list_1))
print(cubed)
