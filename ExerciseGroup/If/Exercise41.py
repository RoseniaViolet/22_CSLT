note = input('Enter the musical note: ')
if note[0] in ('A', 'B', 'C', 'D', 'E', 'F', 'G'):
     if 0 <= int(note[1]) <= 8  :
        if note[0] =='A' :
            Perfect_Fourth = 440.00
        elif note[0] =='B' :
            Perfect_Fourth = 493.88
        elif note[0] =='C' :
            Perfect_Fourth = 261.63
        elif note[0] =='D' :
            Perfect_Fourth = 293.66  
        elif note[0] =='E' :
            Perfect_Fourth = 329.63
        elif note[0] =='F' :
            Perfect_Fourth = 349.23
        elif note[0]=='G' :
            Perfect_Fourth = 392.00    
        F = Perfect_Fourth / (2 ** (4 - int(note[1])))
        print(f'The frequency of {note} is {F}')
     else:
         print('No data on the entered musical note ')
else:
    print('No data on the entered musical note ')
