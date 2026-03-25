# WAP to find the second largest number in an array.

n = int(input("Enter the no. of elements you want to enter: "))
l=[]
for i in range(n):
    a = int(input(f"Enter element {i}: "))
    l.append(a)
print(l)

first = l[0]
second = -1

for i in l:
    if (i>first):
        second = first
        first = i
    elif (i>second and i!=first):
        second = i
print("The second largest number in an array: ",second)
