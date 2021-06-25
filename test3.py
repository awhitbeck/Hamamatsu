import random

response_data_hexstring = ''
for i in range(2):
    x = [random.randint(30, 39), random.randint(41, 46)]  # EXAMPLE response_data_hexstring = 30454139
    response_data_hexstring += str(random.choice(x))

response_data_hexstring = str(random.randint(30, 34)) + response_data_hexstring
if response_data_hexstring[0:2] == '34':
    l = list(response_data_hexstring)
    l[2] = '3'
    l[3] = '0'
    l[4] = '3'
    l[5] = '0'
    response_data_hexstring = "".join(l)

response_data_hexstring = '30' + response_data_hexstring


response_data_val = ''
for i in range(0, len(response_data_hexstring), 2):
    response_data_val += chr(int(response_data_hexstring[i:i + 2], 16))

print(response_data_hexstring)
print(response_data_val)

