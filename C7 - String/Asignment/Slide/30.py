while True:
    p=input()
    if (len(p)<8) or (p.isnumeric()) or (p.isalpha()) or (p.isupper()) or (p.islower()):
        print("Khong hop le!!!")
    else:
        print("Hop le!!!")
        break