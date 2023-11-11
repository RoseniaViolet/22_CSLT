F = float(input('Enter the frequency: '))
note = ''
if abs(F - 440) <= 1:
    note = 'A4'
elif abs(F - 493.88) <= 1:
    note = 'B4'
elif abs(F - 261.63) <= 1:
    note = 'C4'
elif abs(F - 293.66) <= 1:
    note = 'D4'
elif abs(F - 329.63) <= 1:
    note = 'E4'
elif abs(F - 349.23) <= 1:
    note = 'F4'
elif abs(F - 392.00) <= 1:
    note = 'G4'
else:
    print('No data on the entered frequency')
if note:
    print('The note for the entered frequency is:', note)