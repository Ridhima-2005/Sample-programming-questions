# WAP to check if a number is Armstrong number or not
n = int(input("Enter a number: "))
m = n
sum = 0 

while(n>0):
    digit = n%10
    sum = sum + ((digit)**3)
    n = n//10
    
if (sum == m):
    print(f"{m} is an Armstrong number")
else:
    print(f"{m} is not an Armstrong number")