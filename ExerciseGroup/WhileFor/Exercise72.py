string = input("Enter string: ")
first = 0 
last = len(string) - 1
while first < last:
    if string[first] == string[last]:
        first += 1
        last -= 1
    else:
        print("The string is not a palindrome.")
        break
else:
    print("The string is a palindrome.")
