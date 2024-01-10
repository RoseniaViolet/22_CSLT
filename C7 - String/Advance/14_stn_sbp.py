def  list_va_binh_phuong(n):
    dsSTN = [i for i in range(n)]
    dsSBP = [i*i for i in range(n)]
    return dsSTN , dsSBP
def duyet_cac_bien(dsSTN,dsSBP):
    for x in dsSTN:
        print(x,end=' ')
    print()
    for y in dsSBP:
        print(y,end=' ')
try:
    n = int(input())
    if n < 0:
        print('Vui long nhap so tu nhien')
    else:
        dsSTN,dsSBP=list_va_binh_phuong(n)
        duyet_cac_bien(dsSTN,dsSBP)
except:
    print('Dinh dang dau vao khong hop le')
        