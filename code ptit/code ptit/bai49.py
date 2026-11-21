so_hang, so_cot = map(int,input().split())

# TODO 
if so_hang<so_cot :
    for hang in range(1,so_hang+1):
        chieu_ngang = 0
        for cot in range(hang,so_cot+1) :
            print(cot , end = "")
            chieu_ngang += 1
        while chieu_ngang < so_cot :
            print(so_cot-chieu_ngang, end = "")
            chieu_ngang += 1
        print()

elif so_hang==so_cot :
    for hang in range(1,so_hang+1):
        chieu_ngang = 0
        for cot in range(hang,so_cot+1) :
            print(cot , end = "")
            chieu_ngang += 1
        while chieu_ngang < so_cot :
            print(so_cot-chieu_ngang, end = "")
            chieu_ngang += 1
        print()        

elif so_hang >so_cot :
    for hang in range (1,so_hang+1) :
        chieu_ngang = 0
        if hang <= so_cot :
            for cot in range (hang,so_hang+1) :
                if chieu_ngang < so_cot :
                    print(cot,end ="")
                    chieu_ngang += 1
            while chieu_ngang < so_cot :
                print(so_cot-chieu_ngang, end = "")
                chieu_ngang += 1      
        else :
            print(hang , end="")
            chieu_ngang += 1
            while chieu_ngang < so_cot :
                print(so_cot-chieu_ngang, end = "")
                chieu_ngang += 1     
        print()    