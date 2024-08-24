def validPalindrome(s):
    #create a new string variable
    newString = ""

    #for i in s:
    for i in s:
        #if i is alphanumeric
        if i.isalnum():
            #add character to newString
            newString += i.lower()
    #return newString == newString[::-1]
    return newString == newString[::-1]


first = "A man, a plan, a canal: Panama"
second = "race a car"
third = "Anna"

print(validPalindrome(first))
print(validPalindrome(second))
print(validPalindrome(third))