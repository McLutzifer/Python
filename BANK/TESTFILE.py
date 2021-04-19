#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:30:55 2021

@author: lukas
"""


from newreadfile import *

my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"

read_digits = read_file(my_test_file)
#print(len(read_digits))
x = parse_dictionary(read_digits)
print(x)