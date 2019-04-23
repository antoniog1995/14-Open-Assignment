#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-22
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-g',
        '--guess',
        help='Guess string',
        metavar='str',
        type=str, 
        required=True)

    parser.add_argument(
        '-c',
        '--choice',
        help='Word choice',
        metavar='int',
        type=int,
        default=1)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    guess = args.guess.upper()
    choice = args.choice
    
    dict = {1: 'Arcosanti', 2: 'Intercept', 3: 'Positions', 4: 'Collected', 5: 'Gemstones', 6: 'Cellulose', 7: 'Mastodons', 8: 'Meteorite', 9: 'Phoenixes', 10: 'Fireflies'} 
    
    if choice > 10 or choice < 1: 
        die('The choice number must be between 1 and 10') 
    base = dict[choice].upper()
    if len(guess) < len(base) or len(guess) > len(base):
        die('The guess must be the same length as the word: {}'.format(len(base)))
    
    for i,j in zip(guess, base): 
        if i == j:
            print('{}'.format(i),end='') 
        else:
            print('_', end='')
    print('\n') 

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
