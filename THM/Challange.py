# from base64 import *
import base64
import pybase64

print("TEST")

global x

'''
5 times encoded using base 64
5 times encoded using base 32
5 times encoded using base 16!
'''
def code64(x):
    for i in range (5):
        x = base64.b64encode(x)
    return x

def code32(x):
    encodedStr = base64.b64encode(s)
    return encodedStr

def code16(x):
    encodedStr = base64.b64encode(s)
    return encodedStr


file = open('encodedflag.txt', 'r')
text = file.read()

s = text.encode("UTF-8")

for i in range (5):
    x = code64(x)

for i in range (5):
    x = code64(x)

for i in range (5):
    x = code64(x)

print(s)

