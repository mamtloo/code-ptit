so_bo = int(input())
for so in range (so_bo) :
    nhap_so =int(input())
    so_uoc = 0
    while nhap_so >1 :
        if nhap_so %2 == 0 :
            so_uoc +=1
            nhap_so/=2
        else :
            break
    print(so_uoc)    