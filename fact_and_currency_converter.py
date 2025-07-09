# 1) Write a function to find factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5)

print("END 1st example\n")



# 2) Write a function to convert USD to INNR...

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")
          
converter(4)

print("END 2nd example\n")