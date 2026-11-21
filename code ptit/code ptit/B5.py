import sys

input_data = sys.stdin.read().split()

doc = int(input_data[0])
ngang = int(input_data[1])

for i in range(1, doc + 1):
    ket_qua = ''
    if i <= ngang:
        for j in range(i, ngang + 1):
            ket_qua += str(j)
        for j in range(i - 1, 0, -1):
            ket_qua += str(j)
    else:
        ket_qua += str(i)
        for j in range(ngang - 1, 0, -1):
            ket_qua += str(j)
    print(ket_qua)