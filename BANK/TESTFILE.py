#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:30:55 2021

@author: lukas
"""


from newreadfile import *

filename = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"

read_digits = read_file(filename)

parse_dictionary(read_digits)
