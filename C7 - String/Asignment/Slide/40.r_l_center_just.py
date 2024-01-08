TenHang=[]
SoLuong=[]
#Nhap ten hang va so luong
print("Moi nhap ten hang va so luong: ")
for i in range(0,4): # i=(0,1,2,3)
    print("+ Mat hang",i+1,":")
    ten=input(" - Ten hang:")
    TenHang.append(ten)
    sl=input(" - So luong:")    
    SoLuong.append(sl)
for i in range(4):
    a = TenHang[i].ljust(20,'.')
    b = SoLuong[i].rjust(6,' ')
    print(a,end='')
    print(b)

    
    
    
    
# Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tựch, sao cho chiều dài của
# chuỗi đúng bằng n ký tự và chuỗi gốc được đặt nằm bên phải (rjust()), bên trái
# (ljust()) hoặc ở giữa(center()