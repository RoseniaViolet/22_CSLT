vowels = ('a', 'e', 'i', 'o', 'u')
letter = input('Input a letter: ')
if letter.isalpha() and len(letter) == 1:
    if letter in vowels:
        print(f'{letter} is a vowel.')
    elif letter == 'y':
        print(f'{letter} is sometimes a vowel and sometimes a consonant.')
    else:
        print(f'{letter} is a consonant.')
else:
    print('Error: Please enter a single alphabetical character.')
