so_bo = int(input()) 
for so in range(so_bo) :
    tong = 0
    nhap_so = input()
    for chu_so in str(nhap_so) :
        tong += int(chu_so)
    print(tong)