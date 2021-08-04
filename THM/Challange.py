# from base64 import *
import base64
# import pybase64

def thm_base64(x):
    coded = base64.b64decode(x)
    return coded

def thm_base32(x):
    coded = base64.b32decode(x)
    return coded

def thm_base16(x):
    coded = base64.b16decode(x)
    return coded

file = open('encodedflag.txt', 'rb')
flag = file.read()

for i in range(5):
    flag = thm_base16(flag)

for i in range(5):
    flag = thm_base32(flag)

for i in range(5):
    if i != 4:
        flag = thm_base64(flag)
    else:
        flag = thm_base64(flag)
        print(flag)

