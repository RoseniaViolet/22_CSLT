choose = ('tg','ht')
select = str(input())
if select in choose:
    if select == 'tg':
        a = float(input())
        b = float(input())
        c = float(input())
        Stg = a+b+c
        print(Stg)
    if select == 'ht':
        Pi = 3.14
        r = float(input())
        Sht = 2*r*Pi
        print(Sht)