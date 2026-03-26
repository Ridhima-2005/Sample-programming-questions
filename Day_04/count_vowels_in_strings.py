# WAP to print the number of vowels in a string.

s = input("Enter a word or a sentence: ")
v = "aeiouAEIOU"
c = 0
for i in s:
     for j in v: 
        if (i==j):
            c=c+1
print("Total number of vowels are: ",c)