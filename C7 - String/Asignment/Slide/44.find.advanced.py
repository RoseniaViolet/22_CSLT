# nhập từ bàn phims 2 chuỗi st và st2 cho biết st2 xuất hiện bao nhiêu lần trong st1
# không phần biệt chữ hoa và chữ thường
st1="banana"
st2="na"

st1=input("st1: ").lower()
st2=input("st2: ").lower()
dem=0
i=0
while True:
    i=st1.find(st2,i)
    if i>=0:      
        print("Vi tri:",i)
        dem=dem+1
        i=i+1
    else:
        break
   
print("So lan xuat hien:",dem)