# Count digits in a number.
# ex: 
# I/P: 12345
# O/P: 5 
n = int(input("Enter a number: "))
c = 0
while(n>0):
    d = n%10
    c=c+1
    n = n//10
print("Total number of digits are: ",c)