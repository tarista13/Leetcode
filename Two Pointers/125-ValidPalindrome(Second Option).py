def validPalindrome(s):
    #create a left(starts at 0) and right pointer(starts at len(string) - 1)
    l = 0
    r = len(s) - 1
    #while left is less than right:
    while l < r:
        #while left is less than right AND not alphanumeric(s[l]):
        while l < r and not alphaNumeric(s[l]):
            #increment left by 1
            l += 1
        #while right is greater than left AND not alphanumeric(s[r]):
        while r > l and not alphaNumeric(s[r]):
            #decrement right by 1
            r -= 1
        #if s[l].lower != s[r].lower
        if s[l].lower() != s[r].lower():
            #return False
            return False
        #increment left by 1
        l += 1
        #decrement right by 1
        r -= 1
    #return True
    return True

def alphaNumeric(c):
    #return if the character is within "A - Z", "a-z", and "0-9"
    return(
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
    )


first = "A man, a plan, a canal: Panama"
second = "race a car"
third = "Anna"

print(validPalindrome(first))
print(validPalindrome(second))
print(validPalindrome(third))