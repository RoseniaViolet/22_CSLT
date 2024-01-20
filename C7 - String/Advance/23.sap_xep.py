def sap_xep_ds_tang(danh_sach_so):
    L = []
    while len(danh_sach_so) > 0:
        the_min = min(danh_sach_so)
        L.append(the_min)
        danh_sach_so.remove(the_min)
    return L

danh_sach = input().split()
if len(danh_sach) == 0:
    print('Danh sach rong')
else:
    try:
        danh_sach_so = list(map(int,danh_sach))
        L = sap_xep_ds_tang(danh_sach_so)
        print(*L)
    except:
        print('Vui long nhap cac phan tu la so thuc')

