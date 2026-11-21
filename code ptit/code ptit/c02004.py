cao = int(input())
for hang in range (1, cao+1) :
    if hang == 1 or hang == cao :
        print("~" * (cao-hang) + "*" * cao)
    else :
        print("~" * (cao-hang) + "*" + "." * (cao-2) + "*")
        
