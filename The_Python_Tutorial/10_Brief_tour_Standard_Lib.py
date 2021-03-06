import os
print(os.getcwd())
#os.system('mkdir today')
#os.system('touch test.txt')
#os.system('rm test.txt')
#os.system('rm -rf today')

import glob
print(glob.glob('*.py'))


# String pattern matching

import re

x = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(x)


# Mathematics

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))     # sampling without replacement

import statistics
data = [2.75, 1.75, 1.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))

'''
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')   # Decoding the binary data to text
        if 'EST' in line or 'EDT' in line:   # look for eastern time
            print(line)
'''


# Dates and Times

from datetime import date

now = date.today()
print(now)

now = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(now)


# Performance measurement 

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())