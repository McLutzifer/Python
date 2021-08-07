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