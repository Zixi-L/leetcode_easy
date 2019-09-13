
def romanToInt(s):
    symbol_value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  # Be careful! numbers do not need " " 
    result=0
    for r in range(len(s)):
        result += symbol_value[s[r]] # Be aware of this grammar 
        
        if r == 0: continue  #The continue statement continues with the next iteration of the loop,
                             #otherwise we will get r=0 s[r-1]=V
                             # example : https://stackoverflow.com/questions/8420705/example-use-of-continue-statement-in-python
        
        if symbol_value[s[r-1]] < symbol_value[s[r]]:
            result = result - 2*symbol_value[s[r-1]]
            
    return result 
