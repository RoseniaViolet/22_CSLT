# viết chương trình sử dụng hàm
# nhâpj từ bàn phím 3 số nguyên a,b,c
# In lên màn hình số lớn nhất trong 3 số a,b,c
# Khi gọi hàm, nếu truyền 2 tham số thì tìm số lớn nhất của 2 số a và b 
def SLN(a,b,c=None):
    if c==None:
        max=a
        if max<b:
            max=b
    else:
        max=a
        if max<b:
            max=b        
        if max<c:
            max=c            
    print("So lon nhat la:",max)


SLN(5,10,15)    
SLN(5,10)

