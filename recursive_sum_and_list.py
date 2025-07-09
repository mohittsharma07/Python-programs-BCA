# 1) Write a recursive function to calculate the sum of first n natural numbers...

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)

print("END 1st example\n")



# 2) Write a recursive function to print all elements in a list.
# use list and index as parameters

def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)

heroes =  ["ironman","thor","captian america","shaktiman"]
print_list(heroes)

print("END 2nd example\n")