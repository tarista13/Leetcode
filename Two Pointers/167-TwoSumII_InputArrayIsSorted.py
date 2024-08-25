"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numberts be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indicies of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are genereated such taht there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Ex 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Ex 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Ex 3:
Input: numbers = [-1, 0] target = -1
Output: [1,2]
"""

def twoSum(numbers, target):
    l,r = 0, len(numbers) - 1
    while l < r:
        result = numbers[l] + numbers[r]
        if result == target:
            return [l+1, r+1]
        elif result < target:
            l += 1
        else:
            r -= 1


numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [2,3,4]
target2 = 6

numbers3 = [-1, 0]
target3 = -1

print(twoSum(numbers1, target1))
print(twoSum(numbers2, target2))
print(twoSum(numbers3, target3))