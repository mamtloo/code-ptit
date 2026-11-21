import sys

input_data = sys.stdin.read().split()

T = int(input_data[0])

for i in range(T):
    N = int(input_data[i+1])
    day = [int(so) for so in str(N)]
    if day == sorted(day):
        print('YES')
    else:
        print('NO')
