original_word = input('Enter a word to check if it is a palindrome: ')
word = original_word.lower() 

is_palindrome = True
length = len(word)

while length > 1 and is_palindrome:
    if word[0] != word[length - 1]:
        is_palindrome = False
    else:
        word = word[1:length - 1]
        length -= 2

if is_palindrome:
    print(f"The word '{original_word}' is a palindrome.")
else:
    print(f"The word '{original_word}' is not a palindrome.")
