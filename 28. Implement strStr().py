def strStr(self,haystack, needle):  
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i 
    return -1
        
# Time Complexity: O(n*m)
# An improved way to solve this problem is using KMP
# A great explaination of KMP: https://web.stanford.edu/class/cs97si/10-string-algorithms.pdf
# A Video of KMP: https://www.youtube.com/watch?v=BXCEFAzhxGY&feature=youtu.be
