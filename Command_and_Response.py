from serialInterface import *
#import random

test = serialInterface('/dev/ttyUSB1',True)
while 1 > 0:
    test.menu()
    if test.request_com == 'EXT':
        break
    test.commandsList()
