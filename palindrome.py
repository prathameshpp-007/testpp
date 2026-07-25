def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

num = input("Enter a number or string: ")
if is_palindrome(num):
    print(f"'{num}' is a palindrome")
else:
    print(f"'{num}' is not a palindrome")
    
    
    #oo7g
