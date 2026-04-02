# WAP to check if an array is sorted or not.

n = int(input("Enter number of elements of array: "))
arr = []
for a in range(n):
    ele = int(input(f"Enter {a+1} element: "))
    arr.append(ele)
print(arr)

i = 0
isSorted = True
while(i<n-1):
    if arr[i]>arr[i+1]:
        isSorted = False
        break
    i+=1
if (isSorted==True):
    print("Sorted array")
else:
    print("Array is not sorted")

