# WAP to check if the number is palindrome or not.

n = input("Enter a number: ")
isPalindrome = True
l = len(n)
for i in range(l//2):
    if (n[i] == n[l-i-1]):
        isPalindrome = False
        break
if (isPalindrome == True):
    print(f"{n} is not Palindrome")
else:
    print(f"{n} is Palindrome")