from ast import Pass
import random


a = "abcdefghijklmnopqrstvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0124567890"
d = "!@#$%^&*()-=_+"
e = "iutyhbndjgfrelloftybdjmcbvd"
f = "546473048461224368475453736489"
all=a + b + c + d + e + f
length = 20
password = "".join(random.sample(all,length))
print("the password ypu genrated is :", password)
