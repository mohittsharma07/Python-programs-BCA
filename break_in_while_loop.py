# 1)

i = 1
while i <= 10:
    print(i)
    if(i == 8):
        break
    i += 1
    
print("End of loop")




# 2)

nums = (1,4,9,16,25,36,49,64,81,100)

x = 49
i = 0
while i<len(nums):
    if(nums[i] == x): 
       print("found at idx",i )
       break
    else:
        print("Finding...")
    i += 1

print("End of loop")