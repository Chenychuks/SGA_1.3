#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-07-13
Purpose: Dictionary containing keys with values equals to the square of the keys
"""


def square_root():
    count = 4
    while (count < 15):
        count = count + 1
        print({count: count ** 2})


square_root()
