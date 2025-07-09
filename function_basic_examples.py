# 1) print a greeting using simple function...

def print_hello():
    print("Hello")

print_hello()
print_hello()

print("End 1st example\n")


# 2) Calculating the sum of two numbers with returns value...

def calc_Sum(a,b):
    return a + b

Sum = calc_Sum(3,7)
print(Sum)

print("End 2nd example\n")



# 3) Print function calls with different inputs...
    

def calc_Sum(a,b):
    Sum = a + b
    print(Sum)
    return Sum

calc_Sum(7,9)
calc_Sum(4,8)
calc_Sum(77,66)
calc_Sum(39,76)

print("End 3rd example\n")


# 4) print average of 3 numbers...

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

calc_avg(33,44,55)

print("End 4th example\n")