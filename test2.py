from tabulate import tabulate
import random

for i in range(self.y):  # APPENDS THE TABLE IN THE MIDDLE CREATING EMPTY BYTES FOR DATA
    decode[0].append("")
    decode[1].append("")
    for n in range(4):
        decode[0][9 - n + i] = decode[0][8 - n + i]
        encode[1][9 - n + i] = decode[1][8 - n + i]
    decode[0][5 + i] = ""
    decode[1][5 + i] = ""