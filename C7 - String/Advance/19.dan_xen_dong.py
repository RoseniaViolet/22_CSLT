# a:Trang  Ti  , Suu  Eo  ,  Ca  Meo, Dan Beo
# b:Viet Nam, Thai Lan,  Lao , Anh
def xoa_khoang_trang_thua(s):
    result = []
    for x in s:
        result.append(' '.join(x.split()))
    return result

def in_danh_sach(kqT,  kqQT):
   for ten, quocTich in zip(kqT, kqQT):
       print(ten + " - " + quocTich)

dsTen = input().split(',')
dsQuocTich = input().split(',')
if len(dsTen) != len(dsQuocTich):
   print("Vui long nhap hai danh sach cung kich thuoc!")
else:   
    kqT = xoa_khoang_trang_thua(dsTen)
    kqQT = xoa_khoang_trang_thua(dsQuocTich)
    in_danh_sach(kqT, kqQT)



