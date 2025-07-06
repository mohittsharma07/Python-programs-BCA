# 1) Basic list operations.

marks = [78.9, 87.4, 87, 99, 98.9]
print(marks)
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[4])


# 2) Even-odd program in list.

n = int(input("How manay numbers do you want to enter?"))
numbers = [int(input("Enter numbers{i+1}:"))for i in range(n)]

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

print("\n Full list", numbers)
print("Even numbers", even)
print("Odd numbers", odd)