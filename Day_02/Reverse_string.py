# WAP to print reverse of a number
s = int(input("Enter a number: "))
n=s
rev = 0
while s>0:
    digit = s % 10        # extract last digit
    rev = rev * 10 +digit # increment/update reverse value 
    s = s // 10           # removes last digit, making number smaller
print("Original number: ",n)
print("Reversed number: ",rev)
