nhap_so = int(input())
a = list (map(int,input().split()))
chan =[]
le = []
for so in a :
    if int(so)%2 == 0 :
        chan.append(so)
    else :
        le.append(so)
print(*chan)
print(*le)            
