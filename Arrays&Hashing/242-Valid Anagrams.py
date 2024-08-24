""" Given two strings s & t, return true if t is an anagram of s, and false otherwise.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters
    exactly once.

    Ex 1:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Ex 2:
    Input: s = "rat", t = "cat"
    Output: False
"""

def isAnagram(s, t):
    #check to see if s != t:
        #return false
    if len(s) != len(t):
        return False
    
    #create list called countS
    countS = {}
    #create empty list called countT
    countT = {}
    
    # for i in range(len(s)) bc/ both strings are the same length
    for i in range(len(s)):
        #countS[s[i]] = 1 + countS.get(s[i], 0)
        countS[s[i]] = 1 + countS.get(s[i], 0)
        #countT[s[i]] = 1 + countT.get(t[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    #return countS == countT
    return countS == countT


s = "anagram"
t = "nagaram"

h = "rat"
p = "car"

print(isAnagram(s,t))
print(isAnagram(h,p))