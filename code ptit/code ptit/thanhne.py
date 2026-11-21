n = int(input())
nam = n // 365
tuan = (n % 365) // 7
ngay = (n % 365) % 7
print (nam, tuan, ngay)