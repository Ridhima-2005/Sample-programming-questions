# WAP to find maximum number in the list.
n = int(input("Enter the no. of elements you want to enter: "))
l=[]
for i in range(n):
    a = int(input(f"Enter element {i}: "))
    l.append(a)
print(l)
max = l[0]
for i in l:
    if(i>max):
        max = i
print("Maximum element of the list is: " ,max)