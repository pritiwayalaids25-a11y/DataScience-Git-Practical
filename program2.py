text = input("Enter a string: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome")