def select():
    st1 = str(input())
    st2 = str(input())
    st3 = str(input())
    return st1,st2,st3

def checkstring(st1,st2,st3):
    if st1.startswith(st2) or st1.endswith(st3) :
        return True
    else:
        return False

st1,st2,st3 = select()
print(checkstring(st1,st2,st3))


# startswith(str): Trả về True nếu chuỗi bắt đầu bởi chuỗi str;
# endswith(str): Trả về True nếu chuỗi kết thúc bởi chuỗi str, còn lại trả về False;
# Có phân biệt chữ hoa và chữ thường