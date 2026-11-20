so = input()
do_dai = len(so)
so_dau = so[0]
so_cuoi = so[-1]
if so_cuoi == "0" : #chuỗi "0"
    so_moi =so[1:do_dai-1] + so_dau
else :
    so_moi = so_cuoi + so[1:do_dai-1] + so_dau
print(so_moi)