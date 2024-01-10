s = input()
words = s.split()

max_length_word = ""

for word in words:
    if len(word) > len(max_length_word):
        max_length_word = word

print("The longest word is:", max_length_word)
