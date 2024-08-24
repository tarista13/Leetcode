"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Ex 1:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Ex 2:
Input: strs = [""]
Output: [[""]]

Ex 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict

def groupAnagrams(strs):
    #Keep track of all the groups of anagrams
    result = defaultdict(list)

    #Iterate through each string in the list
    for s in strs:
        #Keep track of the count of each letter in the alphabet for each string
        count = [0] * 26
        #iterate through each letter in each string
        for c in s:
            #Add 1 to the count for each letter thats in the string
            count[ord(c) - ord("a")] += 1
        #Add that to the result
        result[tuple(count)].append(s)
    return result.values()

strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2= [""]
strs3 = ["a"]

print(groupAnagrams(strs1))
print(groupAnagrams(strs2))
print(groupAnagrams(strs3))