so_bo =int(input())
for so in range (so_bo) :
    nhap_so = int(input())
    so_ban_dau = nhap_so
    ket_qua = ""
    thua_so = 2
    while thua_so**2 <= so_ban_dau :
        while so_ban_dau % thua_so == 0 :
            ket_qua += str(thua_so) + " "
            so_ban_dau //= thua_so
        thua_so += 1
    #TODO xử lý số cuối cùng
    if so_ban_dau > 1 :
        ket_qua += str(so_ban_dau)
    #TODO Tách số nguyên tố theo khoảng trắng    
    thua_so_nguyen_to = set(ket_qua.split())
    if str(nhap_so) in thua_so_nguyen_to :
        print("YES")
    else :
        print("NO")    
