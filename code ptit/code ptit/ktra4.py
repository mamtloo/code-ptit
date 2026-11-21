so_bo = int(input())
so_khong_giam = True
for so in range (so_bo) :
    nhap_so = input()
    for chu_so in range(len(nhap_so) - 1) :
        if int(nhap_so[chu_so]) > int(nhap_so[chu_so+1]) : #TODO -1 để không nằm ngoài phạm vi
            so_khong_giam = False
            break
        else :
            so_khong_giam = True 

#TODO dùng biến cờ để không bị in hai lần YES NO

    if so_khong_giam == False :
        print("NO")
    else :
        print("YES")
                
