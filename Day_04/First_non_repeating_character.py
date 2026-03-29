# WAP to find the first non-repeating character.

s = input("Enter a string: ")
d = {}

# COUNT FREQUENCY OF AN ELEMENT
for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

# CHECK FIRST APPEARING
for i in s:
    if d[i] == 1:
        print("First non-repeating character is: ",i)
        break
