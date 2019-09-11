def isValid(s: str):
    stack = []
    mapping = {")":"(",
               "}":"{",
               "]":"["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if  mapping[char]!=top_element:
                return False
        else:
            stack.append(char)
    return not stack # here has to be not stack, otherwise '[' will return True. 
                     #ONLY in the case that stack is empthy, return True
print(isValid('()]'))
