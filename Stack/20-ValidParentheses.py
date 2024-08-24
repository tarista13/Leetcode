#create a stack for the opening parentheses
#create a hashmap for the closing parenetheses that are then linked to a opening parentheses:
#if the top of stack equals the closing parenthese, pop from top of stack

"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""

def isValid(s):
    #create a map for corresponding values
    map = {')' : '(', '}' : '{', ']' : '['}
    #create a stack to keep track of opening characters
    stack = []

    #iterate through each character in the string
    for i in s:
        #if it's not a closing bracket, append it to the stack
        if i not in map:
            stack.append(i)
            continue
        #if there's nothing in the stack or the characters don't match, return false
        if not stack or stack[-1] != map[i]:
            return False
        #since it did pass, then you can pop the opening bracket off the stack
        stack.pop()
    return not stack


s1 = "[]"
s2 = "([{}])"
s3 = "[(])"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))