# 1) Print the elements of the following list using a loop..[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1



# 2) Serach for a numbers x in this tuple using loop...(1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)

x = 81
i = 0
while i<len(nums):
    if(nums[i] == x): 
       print("found at idx",i )
    i += 1