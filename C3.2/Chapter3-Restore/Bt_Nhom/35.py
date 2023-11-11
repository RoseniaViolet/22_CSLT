HA= int(input('Enter the number of human years:'))
if HA<0:
    print('error')
elif HA<=2:
    DY=HA*10.5
else:
    DY=2*10.5+(HA-2)*4
print('Dog years:',DY)