from base64 import *

print("TEST")


'''
5 times encoded using base 64
5 times encoded using base 32
5 times encoded using base 16!
'''

file = open('encodedflag.txt', 'r')
text = file.read()


encodedStr = base64encode(file.encode("utf-8"))