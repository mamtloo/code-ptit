so_bo =int(input())
for so in range (so_bo) :
    nhap_so = int(input())
    ket_qua = ""
    thua_so = 2
    while thua_so**2 <= nhap_so :
        while nhap_so % thua_so == 0 :
            ket_qua += str(thua_so) +" "
            nhap_so //= thua_so
        thua_so += 1
    #TODO xử lý số cuối cùng
    if nhap_so > 1 :
        ket_qua += str(nhap_so) 
    print(ket_qua.strip())
    