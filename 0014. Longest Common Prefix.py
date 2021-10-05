def longestprefix(strs):
    shortest = min(strs,key=len) 
    prefix = ''
    for n,l in enumerate(shortest):
        for other in strs:
            if other[n] != l:
                return shortest[:n]
    return shortest
