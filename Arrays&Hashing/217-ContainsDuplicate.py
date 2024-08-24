"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Ex 1:
Input: nums[1,2,3,1]
Output: True

Ex 2:
Input: nums = [1,2,3,4]
Output: False
"""

def containsDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


nums1 = [1,2,3,1]
nums2 = [1,2,3,4]

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))