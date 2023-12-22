while True:
    ten = input()
    if ten.istitle():
        print('Hop le!!!')
        break
    else:
        print('Khong hop le!!!')
# Trả về True nếu chuỗi chỉ chứa các từ,mỗi từ được viết thường và
# viết hoa chữ cái đầu, còn lại trả về False;