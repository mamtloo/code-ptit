canh = int(input())
for hang in range (1,canh+1) :
    if hang ==1 or hang == canh :
        print("*" * canh)
    else :
        print("*" + "." * (canh-2) + "*")    