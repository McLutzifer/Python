# from base64 import *
import base64
import pybase64

print("TEST")


'''
5 times encoded using base 64
5 times encoded using base 32
5 times encoded using base 16!
'''

file = open('encodedflag.txt', 'r')
text = file.read()

s = text.encode("UTF-8")

for i in range (5):
    encodedStr = base64.b64encode(s)
    s = encodedStr

for i in range (5):
    encodedStr = base64.b32encode(s)
    s = encodedStr


for i in range (5):
    encodedStr = base64.b16encode(s)
    s = encodedStr

print(s)