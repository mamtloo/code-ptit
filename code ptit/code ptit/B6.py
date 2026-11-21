import sys

input_data = sys.stdin.read().split()

T = int(input_data[0])

for i in range(1, T+1):
    N = int(input_data[i])
    tong = sum(int(x) for x in str(N))
    if tong % 10 == 0:
        print('YES')
    else:
        print('NO')