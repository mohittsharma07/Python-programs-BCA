# 1) Countdown using recursion...

def show(n):
    if(n == 0):
        return
    print (n)
    show(n-1)

show(10)


print("END 1st program\n")



# 2) Program for factorial using recursion...

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n - 1) * n

print(fact(7))

print("END 2nd program\n")