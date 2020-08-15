# program is for checking the string is palindrome is or not.

def ispalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
        
s=input()
if ispalindrome(s)==True:
    print("It is palindrome")
else:    
    print("It is not palindrome")