def removeElement(self, nums: List[int], val: int) -> int:
    
    # function of slow point: always points to the target number(val) in the loop 
    slow=0
    
    for i in nums:
        # no operation when i == val
        # move the number which ≠ val to the front of the list
        if i != val:
            nums[slow]=i
            slow +=1
    return slow
