# Write a program to find the factorial of first natural numbers... 
# using for loop :-
n = int(input("Enter number"))
fact = 1

for i in range(1,n+1):
    fact *= i

print("factorial =",fact)



# Using while loop :-

n = int(input("Enter number"))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("factorial =",fact)