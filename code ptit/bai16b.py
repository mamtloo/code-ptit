so_bo_test = int(input())
for so_thu in range (so_bo_test) :
    nhap_so = input().strip()
    if nhap_so[0] == nhap_so[-1] :
        print("YES")
    else :
        print("NO")    