import sys

input_data = sys.stdin.read().split()

rong = int(input_data[0])
cao = int(input_data[1])

for i in range(cao):
    if i+1 == 1 or i+1 == cao:
        print('*'*rong)
    else:
        print('*' + ' '*(rong-2) + '*')