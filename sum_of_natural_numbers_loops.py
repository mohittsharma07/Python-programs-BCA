# Write a program to find a sum of first natural numbers...
# Using for loop :-

n = int(input("Enter number"))
sum = 0

for i in range(1,n+1):
    sum += i

print("Total sum =",sum)



# Using while loop:-

n = int(input("Enter number"))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1


print("Total sum =",sum)