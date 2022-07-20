#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-07-13
Purpose: Exponentiation
"""

import argparse


# --------------------------------------------------
def expo():
    '''Exponentiation'''
    print('Exponentiation')

    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Enter the int of x and y',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('x',
                        metavar='x',
                        help='Enter int for x')
                        
    parser.add_argument('y',
                        metavar='y',
                        help='Enter int for y')             
    

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = expo()
    x=args.x
    y=args.y

    if int(y) == 0:
        print(1)
    else:
        x=int(x)**int(y)
        print(x)
        

# --------------------------------------------------
if __name__ == '__main__':
    main()

