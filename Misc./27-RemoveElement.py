def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
    
    

nums = [3,2,2,3]
val = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

print(removeElement(nums, val))
print(removeElement(nums2, val2))