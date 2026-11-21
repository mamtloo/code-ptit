nhap_ten = input().lower().strip()
thanh_phan = nhap_ten.split()
ho = thanh_phan[0]
do_dai =len(thanh_phan)
ten = thanh_phan[-1]
email = ho[0] 
for i in range (1 , do_dai-1):
    ten_dem = thanh_phan[i]
    email += ten_dem[0]
email += ten +"@ptit.edu.vn"     
print(email)    