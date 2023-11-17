read_letter = input("Enter a letter: ")
vowels = "aeiou"
if read_letter.lower() in vowels:
    print(f"{read_letter} is a vowel.")
elif read_letter.lower() == "y":
    print(f"{read_letter} is sometimes a vowel, sometimes a consonant.")
else:
    print(f"{read_letter} is a consonant.")
