import sys


def so_chan_dac_biet(num):
    if num % 2 == 1:
        return False
    day = []
    for so in str(num):
        if int(so) % 2 == 0:
            day.append(so)
    return len(day) == len(str(num))

input_data = sys.stdin.read().split()

T = int(input_data[0])

for i in range(1,T+1):
    N = int(input_data[i])
    if so_chan_dac_biet(N):
        print('YES')
    else:
        print('NO')