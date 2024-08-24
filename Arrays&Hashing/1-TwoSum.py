def twoSum(nums, target):
    #create a map of the previous elements within the array Nums (val:index)
    prevMap = {}

    #create a for loop for two variables in enumerate(nums)
    for i, n in enumerate(nums):
        #have a variable difference equal to the target number - n
        diff = target - n
        #if the difference is in the hashmap
        if diff in prevMap:
            #return the indicies of both elements
            return [prevMap[diff], i]
        #have prevMap[n] equal i
        prevMap[n] = i
    return False


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))