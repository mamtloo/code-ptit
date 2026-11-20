rong , cao   = map(int, input().split())
for don_vi in range(cao) :
    if don_vi == 0 or don_vi == cao -1  :
        print("*" * rong)
    else :
        if rong == 1 :
            print("*")
        else : 
            print("*"+" "*(rong-2)+"*")         