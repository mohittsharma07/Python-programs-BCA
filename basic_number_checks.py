# Write a program to check if a number entered by the user is odd or even.

num = int(input("Enter number"))

if(num % 2 == 0):
    print("This number is even")
else:
    print("This number is odd")

print("\n--------------------\n")


# Write a program to find the greatest of 3 numbers entered by the user.

a = int(input("Enter First number"))
b = int(input("Enter Second number"))
c = int(input("Enter Third number"))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third number is largest", c)

print("\n--------------------\n")


# Write a program to check if a number is a multiple of 9 or not.

m = int(input("Enter number: "))

if (m % 9 == 0):
    print("multiple of 9")
else:
    print("This number not a multiple ")

