def twoSum(target,nums):
    ht = {}
    for i in range(len(nums)):
        if nums[i] in ht:
            return(ht[nums[i]],i)
        else:
            # here is i not nums[i]. Otherwise will return the numebr in the list, not the index
            ht[target-nums[i]] = i 
    return False
print(twoSum(9,[2, 7, 11, 15]))
