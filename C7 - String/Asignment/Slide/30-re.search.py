import re

def check_password(password):
    if not len(password) > 8 :
        return 'Không hợp lệ'
    elif not re.search('[a-z]', password):
        return 'Không hợp lệ'
    elif not re.search('[0-9]', password):
        return 'Không hợp lệ'
    elif not re.search('[A-Z]', password):
        return 'Không hợp lệ'
    else:
        return 'Hợp lệ'
    
while True:    
    password = input()
    print(check_password(password))
    if check_password(password) == 'Hợp lệ':
        break
