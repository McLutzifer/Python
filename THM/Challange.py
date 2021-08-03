# from base64 import *
import base64
# import pybase64

def thm_base64(x):
    coded = base64.b64encode(x)
    return coded

def thm_base32(x):
    coded = base64.b32encode(x)
    return coded

def thm_base16(x):
    coded = base64.b16encode(x)
    return coded

file = open('encodedflag.txt', 'r')
text = file.read()

for i in range(5):
    flag = thm_base64(flag)

for i in range(5):
    flag = thm_base64(flag)

for i in range(5):
    flag = thm_base64(flag)


print(x)

