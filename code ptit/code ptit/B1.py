import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 2:
    a = int(input_data[0])
    b = int(input_data[1])
    if b == 0:
        print(0)
    else:
        tong = a + b
        hieu = a - b
        tich = a * b
        thuong = a / b
        chia_phan_du = a % b
        print(tong, hieu, tich, f"{thuong:.2f}", chia_phan_du)