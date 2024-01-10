def ds_ptu_duy_nhat(danhSach):
    Ptuduynhat = ''
    for i in danhSach:
        if danhSach.count(i) == 1:
            Ptuduynhat += str(i)
    return Ptuduynhat
def xu_ly_dinh_dang(Ptuduynhat):
    for x in Ptuduynhat:
        print(x,end=' ')
        
danhSach = input().split()
Ptuduynhat=ds_ptu_duy_nhat(danhSach)
xu_ly_dinh_dang(Ptuduynhat)
# 1 2 1 2 3 4 
# '1' '2' '1' '2' '3' '4'
# i=1  1 - ko có : 1
# i=2  1 - có