while True:
    password = input()
    
    if (len(password) > 8  and
        any(char.isalpha() for char in password) and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password)):
        print('Hợp lệ')
        break
    else:
        print('Không hợp lệ.')
