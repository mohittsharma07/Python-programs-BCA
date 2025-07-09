# Write a function to print the length of a list.( list is the parameter)

Cities = ["kanpur","lucknow","noida","pune","gurgaon","mumbai","chenni"]
Heroes = ["ironman","thor","captian america","shaktiman"]

def print_len(list):
    print(len(list))

print_len(Cities)
print_len(Heroes)


print("END 1st example\n")



# 2) Write a function to print the elements of a list in a single line. (list is the parameter)

Cities = ["kanpur","lucknow","noida","pune","gurgaon","mumbai","chenni"]
Heroes = ["ironman","thor","captian america","shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end =" ")

print_list(Heroes)
print()

print("END 2nd example\n")
