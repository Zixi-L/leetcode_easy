def strStr(self,haystack, needle):  
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i 
    return -1
        
        
        
print(search([1,3,5,6], 4))
