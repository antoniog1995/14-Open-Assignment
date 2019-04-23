#!/usr/bin/env python3
"""
Author : antoniogutierrez-jaramillo
Date   : 2019-04-22
Purpose: Rock the Casbah
"""


from subprocess import getstatusoutput, getoutput
import os
import sys
import re 

prg = './Hangman.py'

#-------------------------------------------------

#-------------------------------------------------
def test_usage():
    """usage"""
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)

#-------------------------------------------------
def test_bad_args(): 
    """die on bad args"""
    rv1, out1 = getstatusoutput(prg) 
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)
    
    rv2, out2 = getstatusoutput('{} -g ARCOLOGIS'.format(prg))
    assert rv2 == 0
    assert re.match("ARCO_____\n", out2, re.IGNORECASE)
    
    rv3, out3  =getstatusoutput('{} -g arcology'.format(prg))
    assert rv3 > 0
    assert re.match("The guess must be the same length as the word: 9", out3, re.IGNORECASE)
    
#-------------------------------------------------
def test_good_one():

    rv, out = getstatusoutput('{} -c 1 -g Arcosanti'.format(prg))
    assert rv == 0
    assert re.match('ARCOSANTI\n', out,re.IGNORECASE) 

#-------------------------------------------------
def test_good_two():

    rv, out = getstatusoutput('{} -c 2 -g Intercept'.format(prg))
    assert rv == 0
    assert re.match('INTERCEPT\n', out,re.IGNORECASE)
    
#-------------------------------------------------
def test_good_three():
    rv, out = getstatusoutput('{} -c 3 -g Positions'.format(prg))
    assert rv == 0
    assert re.match('POSITIONS\n', out,re.IGNORECASE)

#-------------------------------------------------
def test_good_four():
    rv, out = getstatusoutput('{} -c 4 -g Collected'.format(prg))
    assert rv == 0
    assert re.match('COLLECTED\n', out,re.IGNORECASE)
    
#-------------------------------------------------
def test_good_five():
    rv, out = getstatusoutput('{} -c 5 -g Gemstones'.format(prg))
    assert rv == 0
    assert re.match('GEMSTONES\n', out,re.IGNORECASE)
    
#-------------------------------------------------
def test_good_six():
    rv, out = getstatusoutput('{} -c 6 -g Cellulose'.format(prg))
    assert rv == 0
    assert re.match('CELLULOSE\n', out,re.IGNORECASE)
    
#-------------------------------------------------
def test_good_seven():
    rv, out = getstatusoutput('{} -c 7 -g Mastodons'.format(prg))
    assert rv == 0
    assert re.match('MASTODONS\n', out,re.IGNORECASE)
    
#-------------------------------------------------
def test_good_eight():
    rv, out = getstatusoutput('{} -c 8 -g Meteorite'.format(prg))
    assert rv == 0
    assert re.match('METEORITE\n', out,re.IGNORECASE)
#-------------------------------------------------
def test_good_nine():
    rv, out = getstatusoutput('{} -c 9 -g Phoenixes'.format(prg))
    assert rv == 0
    assert re.match('PHOENIXES\n', out,re.IGNORECASE)

#-------------------------------------------------
def test_good_ten():
    rv, out = getstatusoutput('{} -c 10 -g Fireflies'.format(prg))
    assert rv == 0
    assert re.match('FIREFLIES\n', out,re.IGNORECASE)

