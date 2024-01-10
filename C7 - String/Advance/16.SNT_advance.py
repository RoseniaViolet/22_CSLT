def kt_so_nguyen_to(n):
   if n < 2:
       return False       
   for i in range(2, n):
       if n % i == 0:
           return False
   return True

def ds_so_nguyen_to(danhSachSo):
    for i in danhSachSo:
        if kt_so_nguyen_to(i) == True:
            dsSoNguyenTo.append(i)
    return dsSoNguyenTo

danhSach = input().split()
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   try:
       dsSoNguyenTo = []
       danhSachSo = list(map(int, danhSach))
       dsSoNguyenTo = ds_so_nguyen_to(danhSachSo)
       print(*dsSoNguyenTo)
   except:
       print("Vui long nhap cac phan tu la so nguyen!")
