so = input()
tong = 0
for chu_so in so :
    tich = 1
    #TODO tính giai thừa từng chữ số
    for phan_tu in range (1,int(chu_so)+1) :
        tich = tich * phan_tu
    tong += tich
if int(so) == tong :
    print("1")
else :
    print("0")            

