# Given a list of numbers, find the sum of all elements
n = int(input("Enter the no. of elements you want to enter: "))
l=[]
sum = 0
for i in range(n):
    a = int(input(f"Enter element {i}: "))
    l.append(a)
print(l)
for i in l:
    sum = sum+i
print(sum)