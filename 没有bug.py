def strStr(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i-1
    return -1

print(strStr('hello','ll'))
                   
