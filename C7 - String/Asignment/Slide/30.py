while True:
    password = input()

    if len(password) < 8:
        print('Không hợp lệ.')
    elif not any(char.isalpha() for char in password):
        print('Không hợp lệ.')
    elif not any(char.isdigit() for char in password):
        print('Không hợp lệ.')
    elif not any(char.isupper() for char in password):
        print('Không hợp lệ.')
    elif not any(char.islower() for char in password):
        print('Không hợp lệ.')
    else:
        print('Hợp lệ')
        break
