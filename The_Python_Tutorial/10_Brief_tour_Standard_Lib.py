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