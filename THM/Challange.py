# from base64 import *
import base64
import pybase64


'''
5 times encoded using base 64
5 times encoded using base 32
5 times encoded using base 16!


def code32(x):
    x = base64.b64encode(x)
    return x

def code16(x):
    x = base64.b64encode(x)
    return x
'''


file = open('encodedflag.txt', 'r')
text = file.read()

x = text.encode("UTF-8")

x = base64.b64encode(x)
'''
x = base64.b64encode(x)
x = base64.b64encode(x)
x = base64.b64encode(x)
x = base64.b64encode(x)

x = base64.b32encode(x)
x = base64.b32encode(x)
x = base64.b32encode(x)
x = base64.b32encode(x)
x = base64.b32encode(x)

x = base64.b16encode(x)
x = base64.b16encode(x)
x = base64.b16encode(x)
x = base64.b16encode(x)
x = base64.b16encode(x)
'''

print(x)

