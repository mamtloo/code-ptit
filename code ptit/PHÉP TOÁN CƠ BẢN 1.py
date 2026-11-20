a, b = map(int, input().split())
if b == 0 :
    print("0")
else :
    print(a+b,a-b,a*b,f"{a/b:.2f}",a%b)