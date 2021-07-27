import os
print(os.getcwd())
os.system('mkdir today')
os.system('touch test.txt')
os.system('rm test.txt')
os.system('rm -rf today')