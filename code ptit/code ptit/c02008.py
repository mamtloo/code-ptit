cao = int(input())
for hang in range (1, cao+1) :
    if hang ==1 : 
        print("*" * hang)
    elif hang == cao :
        print("*" * hang)
    else :
        print("*" + "." * (hang-2) + "*")    
        