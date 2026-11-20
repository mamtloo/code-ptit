import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
pascal = []

for i in range(N):
    cot = [1] * (i+1)
    for j in range(1,i):
        cot[j] = pascal[i-1][j-1] + pascal[i-1][j]
    pascal.append(cot)
    print(*cot)    