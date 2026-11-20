import sys


def phan_tich(n):
    thua_so = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            thua_so.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        thua_so.append(n)
    return thua_so

input_data = sys.stdin.read().split()

T = int(input_data[0])
for i in range(1, T+1):
    n = int(input_data[i])
    ket_qua = phan_tich(n)
    thong_ke = {}
    for so in ket_qua:
        thong_ke[so] = thong_ke.get(so, 0) + 1
    print(f'Test {i}:',end=' ')
    for so, so_lan in thong_ke.items():
        print(f"{so}({so_lan})" , end=' ')

    print()