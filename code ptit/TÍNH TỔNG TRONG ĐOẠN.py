a,b = map(int,input().split())
tong = 0
if a < b :
    for so in range(a,b+1) :
        tong += so
elif a > b :
    for so in range (b,a+1) :
        tong += so
print(tong)