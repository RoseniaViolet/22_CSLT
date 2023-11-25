def is_prime(num):
    for i in range(2, num):
        if num % i == 0 and num != 2:
            return False
    return True

def So_lan():
    Thuc_hien = int(input('n='))
    return Thuc_hien

def SNT():
    n = So_lan()
    Dem = 0
    a = 2
    while Dem < n:
        if is_prime(a) == True:
            print(a, end=', ' if Dem < n - 1 else '')
            Dem += 1
        a += 1

SNT()

