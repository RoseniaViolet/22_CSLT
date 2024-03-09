def kt_so_nguyen_to(n):
   if n < 2:
       return False       
   for i in range(2, n):
       if n % i == 0:
           return False
   return True

def ds_so_nguyen_to(danhSachSo):
    for i in danhSachSo:
        if kt_so_nguyen_to(i) == False:
            return False
    return True

danhSachSo = []
for _ in range(2):
    a = int(input())
    danhSachSo.append(a)

ketqua = ds_so_nguyen_to(danhSachSo)
print(ketqua)


