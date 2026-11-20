nhap_so = int(input())
ket_qua = ""
thua_so = 2
while thua_so**2 <= nhap_so :
    while nhap_so % thua_so == 0 :
        ket_qua += str(thua_so) +"x"
        nhap_so //= thua_so
    thua_so += 1
#TODO xử lý số cuối cùng
if nhap_so > 1 :
    ket_qua += str(nhap_so)
#TODO trường hợp số 8 sẽ ra 2x2x2x
else :
    ket_qua = ket_qua[:-1]    
print(ket_qua.strip())  