def containsDuplicate(nums):
    #create a hashset to contain the numbers
    hashset = set()

    #for i in nums:
    for i in nums:
        #if i is already in hashset:
        if i in hashset:
            #return true
            return True
        #add i to hashset
        hashset.add(i)
    #return False
    return False


nums = [1,2,3,1]
next = [1,2,3,4]
digits = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums))
print(containsDuplicate(next))
print(containsDuplicate(digits))