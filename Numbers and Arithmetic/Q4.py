#Check if No is Palindrome

n = input("Enter a number: ")
if n == n[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")
