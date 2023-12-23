import re

def check_password(password):
    if not 6 <= len(password) <= 17:
        return False
    elif not re.search('[a-z]', password):
        return False
    elif not re.search('[0-9]', password):
        return False
    elif not re.search('[A-Z]', password):
        return False
    elif not re.search('[$#@]', password):
        return False
    else:
        return True

password = input()
print(check_password(password))



# Sử dụng hàm re.search("[a-z]",st) cho phép kiểm tra các ký tự trong chuỗi st có chứa chữ cái 
# trong tập [a-z] hay không. Dùng lệnh Import re để khai báo thư viện re
