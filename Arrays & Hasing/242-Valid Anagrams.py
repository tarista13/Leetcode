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