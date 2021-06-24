import random

x = '0000'
y = ''

for i in range(4):
     y += hex(ord(x[i:i+1]))[2:]

print(y)
