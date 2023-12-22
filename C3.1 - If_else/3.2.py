M1= int(input('M1='))
M2= int(input('M2='))
M3= int(input('M3='))
S= int(input('S='))
if S<=100: 
    T= M1*S
if 101<= S <= 150:
    T= M1*100 + (S-100)*M2
if S >= 151:
    T= M1*100 + M2*50 + (S-150)*M3
print('Phai tra=', T, sep='')