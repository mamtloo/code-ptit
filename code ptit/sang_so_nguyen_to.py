so_bo_test = int(input())
for so in range (so_bo_test) :
    nhap_so = int(input())
    so_nguyen_to = [True] * (nhap_so+1)
    so_nguyen_to[0] = so_nguyen_to[1] = False
    so_hien_tai = 2
    while so_hien_tai ** 2 <= nhap_so :
        if so_nguyen_to[so_hien_tai] :
            for boi_so in range (so_hien_tai*2,nhap_so+1,so_hien_tai) :
                so_nguyen_to[boi_so] = False
            so_hien_tai += 1

    if so_nguyen_to[nhap_so] :
        print("YES")    
    else :
        print("NO")    