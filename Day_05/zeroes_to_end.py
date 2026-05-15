# WAP to move all the zeroes to the end.

n = int(input("Enter number of elements of array: "))
arr = []
for a in range(n):
    ele = int(input(f"Enter {a+1} element: "))
    arr.append(ele)
print("Original list: ",arr)

for i in arr:
    if (i == 0):
        arr[i] = arr[i+1]
        arr[-1] = arr[i]
print("No element is zero")
print(f"Final array is: {arr}")